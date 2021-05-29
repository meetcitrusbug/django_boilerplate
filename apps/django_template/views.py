from functools import total_ordering
import re
from django.http.response import JsonResponse
import stripe
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from customadmin.models import Plan, PlanFeature, Card, SubscriptionOrder, UserProfile
from django_boilerplate.settings import CURRENCY
from .forms import CardAddForm
from django.db.models import Q
from django.conf import settings
from django.db.models import Sum
from django.db.models import F
from customadmin.stripe import MyStripe
from django_boilerplate.models import User
import datetime
from dateutil import relativedelta


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            plans = Plan.objects.all().order_by('created_at')
            user_plan = UserProfile.objects.filter(user=request.user).first()
            for plan in plans:
                plan.plan_features = PlanFeature.objects.filter(plan=plan)
            context = {
                'plans':plans,
                'currency':CURRENCY,
                'user_plan':user_plan
            }
            return render(request, 'django_template/index.html', context)
        return redirect('login')


class LoginPageView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request=request, template_name="django_template/userlogin.html", context={"login_form":form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                return redirect('login')
        else:
            return redirect('login')


def userlogout(request):
    logout(request)
    return redirect('login')


class AddCardView(View):
    
    template_name = "django_template/add_card.html"
    model = Card
    form = CardAddForm
    kwargs = {}
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, self.get_context_data())
        return redirect('login')
    
    def get_context_data(self):
        self.kwargs['form'] = self.form
        return  self.kwargs
        
        
    def post(self, request):
        form = self.form(data=request.POST, request=request)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Card added")
                print('kjflsdjflsdkfjsdljkf')
                return redirect('cards')    
            except Exception as e:
                messages.error(request, str(e))

            context_data = self.get_context_data()
            context_data['form'] = form
            return render(request, self.template_name, context_data)
        else:
            context_data = self.get_context_data()
            context_data['form'] = form
            return render(request, self.template_name, context_data)


class CardsList(View):
    
    template_name = 'django_template/card.html'
    model = Card
    ordering = ["id"]

    def get(self, request, *args, **kwargs):
        self.kwargs = kwargs
        self.request = request
        if request.user.is_authenticated:
            return render(request, self.template_name, self.get_context_data())
        return redirect('login')
    

    def get_context_data(self):
        self.kwargs['list'] = self.get_queryset()
        self.kwargs['search'] = self.request.GET.get('search')
        return  self.kwargs
    
    def get_queryset(self):
        search = self.request.GET.get('search')
        query = self.model.objects.filter(user=self.request.user).order_by('-id')

        if search :
            return query.filter(
                Q(card_number=search)
            )
        return query
    

class CardDeletView(View):
    
    model = Card
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    def get(self, request, pk):
        instance = self.get_object(pk)
        if instance:
            try:
                stripe.Customer.delete_source(
                        instance.user.credentials,
                        instance.stripe_card_id,
                        )
                self.perform_destroy(instance)
                messages.success(request, 'Card deleted')
                return redirect('cards') 
            except Exception as e:
                messages.success(request, 'Can not delete card')
                return redirect('cards') 
        messages.success(request, 'Card not found')
        return redirect('cards') 
            
    def get_object(self, pk):
        return self.model.objects.filter(pk=pk).first()
    
    def perform_destroy(self, instance):
        instance.delete()

class CheckoutWithCardView(View):

    def get(self, request, pk):
        if request.user.is_authenticated:
            plan = Plan.objects.get(pk=pk)
            cards = Card.objects.filter(user=request.user)
            if cards:
                return render(request, 'django_template/checkout.html', {'plan':plan,'cards':cards})
            return redirect('card-add')
        return redirect('login')
    
    
    def post(self, request, pk):
        stripe = MyStripe()
        subscription=Plan.objects.get(pk=pk)
        card = Card.objects.get(pk=request.POST.get('card'))
        user_obj = User.objects.filter(id=request.user.id).first()
        user_plan = UserProfile.objects.filter(user__id=request.user.id).first()


        subscribe_new_plan = stripe.subscribePlan(
                request.user.credentials,
                subscription.stripe_plan_id,
                card.stripe_card_id,
            )
        nextmonth = datetime.datetime.today() + relativedelta.relativedelta(months=subscription.duration_in_months)
        if subscribe_new_plan["status"] == "active":
            if user_plan.subscription:
                subscription_order = SubscriptionOrder.objects.filter( user__id=user_obj.id,
                            stripe_subscription_id=user_plan.stripe_subscription_id,
                            plan_status="active",
                        )
                subscription_stripe = stripe.CancelSubscriptionPlan(
                    user_plan.stripe_subscription_id
                )
                for cancel in subscription_order:
                    sub_object = (
                        subscription_cancel_order
                    ) = SubscriptionOrder.objects.filter(id=cancel.id).first()
                    sub_object.plan_status = "cancel"
                    sub_object.save()
            subscripton_data = {
                    "user": request.user,
                    "subscription": subscription,
                    "amount": subscription.plan_amount,
                    "charge_id": subscribe_new_plan["id"],
                    "ordre_status": "success",
                    "plan_status": "active",
                    "stripe_subscription_id": subscribe_new_plan["id"],
                    "expire_date": nextmonth,
                }
            user_plan.subscription = subscription
            user_plan.stripe_subscription_id = subscribe_new_plan["id"]
            user_plan.save()

            subscription_new = SubscriptionOrder.objects.create(
                        **subscripton_data
                    )
            return JsonResponse(
                        {
                            "status": "OK",
                            "message": "Old subscription has been cancelled & new subscription started now",
                        }
                    )


class CancelSubscriptionView(View):
    def get(self, request):
        user_plan = UserProfile.objects.filter(user=request.user).first()
        context = {
            'currency':CURRENCY,
            'user_plan':user_plan
        }
        return render(request, 'django_template/cancel_sub.html',context)
    def post(self, request):
        stripe = MyStripe()
        try:
            stripe = MyStripe()
            user_obj = User.objects.filter(id=request.user.id).first()
            user_plan = UserProfile.objects.filter(user__id=request.user.id).first()

            if not user_plan.subscription:
                return JsonResponse(
                    {
                        "status": "OK",
                        "message": "No subscription plan active now.",
                        "data": [],
                    }
                )

            subscription_order = SubscriptionOrder.objects.filter(
                user__id=user_obj.id,
                stripe_subscription_id=user_plan.stripe_subscription_id,
                plan_status="active",
            )

            for cancel in subscription_order:
                sub_object = SubscriptionOrder.objects.filter(id=cancel.id).first()
                sub_object.plan_status = "cancel"
                sub_object.save()


            stripe = MyStripe()
            subscription_stripe = stripe.CancelSubscriptionPlan(
                user_plan.stripe_subscription_id
            )
            user_plan.subscription = None
            user_plan.stripe_subscription_id = ""
            user_plan.save()
            return JsonResponse(
                {"status": "OK", "message": "Subscription cancelled ", "data": []}
            )

        except Exception as e:
            return JsonResponse({"status": "FAIL", "message": str(e), "data": []})
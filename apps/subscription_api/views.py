import datetime
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, AllowAny

import stripe as stripeErr
from customadmin.models import (
    Plan,
    Card,
    SubscriptionOrder,
    UserProfile,
)
from dateutil import relativedelta
from customadmin.stripe import MyStripe
from django_boilerplate.models import User

from .serializer import (
    SubscriptionPlanSerializer,
    CardSerializer,
    SubscriptionOrderSerializer,
    UserProfileSerializer,
    UserDetailsSerializer,
)
from .apiviews import MyAPIView


# .................................
# .................................................................................
# Subscription Plan API
# .................................................................................


class SubscriptionPlanListAPIView(MyAPIView):

    """
    API View for Subscription Plan listing
    """

    permission_classes = (AllowAny,)
    serializer_class = SubscriptionPlanSerializer

    def get(self, request, format=None):

        try:
            plan = Plan.objects.all().order_by("plan_amount")
            serializer = self.serializer_class(
                plan, many=True, context={"request": request}
            )
            return Response(
                {
                    "status": "OK",
                    "message": "Successfully fetched subscription plan list",
                    "data": serializer.data,
                }
            )

        except:
            return Response(
        {"status": "FAIL", "message": "Subscription plan not found", "data": []}
        )


class ChangeCurrentSubscriptionAPI(MyAPIView):

    """API View to create Card"""

    permission_classes = (IsAuthenticated,)
    serializer_class = CardSerializer
    def post(self, request, format=None):

        """POST method to create the data"""

        if request.user.is_authenticated:

            try:
                stripe = MyStripe()
                user_obj = User.objects.filter(id=request.user.id).first()
                user_plan = UserProfile.objects.filter(user__id=request.user.id).first()
                subscription = Plan.objects.filter(
                    id=request.data["subscription"]
                ).first()
                card = Card.objects.filter(user__id=request.user.id).first()
                user_serilizer = UserDetailsSerializer(user_obj)
                user_plan_serializer = UserProfileSerializer(user_plan)

                if not user_plan.subscription:
                    return Response(
                        {"status": "OK", "message": "No subscription plan active now.", "data":[]}
                    )

                if not request.user.credentials:
                    new_stripe_customer = stripe.createCustomer(request.user)
                    user_obj.credentials = new_stripe_customer["id"]
                    user_obj.save()

                if not card:
                    return Response(
                        {
                            "status": "OK",
                            "message": "Please update card details",
                            "data": [],
                        }
                    )

                subscribe_new_plan = stripe.subscribePlan(
                    user_obj.credentials,
                    subscription.stripe_plan_id,
                    card.stripe_card_id,
                )
                nextmonth = datetime.datetime.today() + relativedelta.relativedelta(months=subscription.duration_in_months)

                if subscribe_new_plan["status"] == "active":

                    if user_plan.subscription:

                        subscription_order = SubscriptionOrder.objects.filter(
                            user__id=user_obj.id,
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

                        context = {
                            "user": user_serilizer.data,
                            "user_plan": user_plan_serializer.data,
                        }
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

                    serializer = SubscriptionOrderSerializer(subscription_new)

                    subscriptin_serializer = SubscriptionOrderSerializer(
                        subscription_new
                    )
                    context = {
                        "user": user_serilizer.data,
                        "subscription_order": subscriptin_serializer.data,
                    }

                    return Response(
                        {
                            "status": "OK",
                            "message": "Old subscription has been cancelled & new subscription started now",
                            "data": serializer.data,
                        }
                    )

            except stripeErr.error.CardError as e:

                body = e.json_body
                err = body.get("error", {})

                return Response(
                    {"status": "FAIL", "message": err["message"], "data": []}
                )

            except stripeErr.error.AuthenticationError as e:

                body = e.json_body
                err = body.get("error", {})
                return Response(
                    {"status": "FAIL", "message": err["message"], "data": []}
                )

            except stripeErr.error.InvalidRequestError as e:
                body = e.json_body
                err = body.get("error", {})
                return Response(
                    {"status": "FAIL", "message": err["message"], "data": []}
                )

            except Exception as e:
                return Response({"status": "FAIL", "message": str(e), "data": []})


class CancelSubscriptionAPI(MyAPIView):

    """API View to create Card"""

    permission_classes = (IsAuthenticated,)
    serializer_class = CardSerializer

    def post(self, request, format=None):

        """POST method to create the data"""

        if request.user.is_authenticated:

            try:
                stripe = MyStripe()
                user_obj = User.objects.filter(id=request.user.id).first()
                user_plan = UserProfile.objects.filter(user__id=request.user.id).first()

                if not user_plan.subscription:
                    return Response(
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

                context = {
                    "user": user_serilizer.data,
                    "user_plan": user_plan_serializer.data,
                }

                stripe = MyStripe()
                subscription_stripe = stripe.CancelSubscriptionPlan(
                    user_plan.stripe_subscription_id
                )
                user_plan.subscription = None
                user_plan.stripe_subscription_id = ""
                user_plan.save()
                return Response(
                    {"status": "OK", "message": "Subscription cancelled ", "data": []}
                )

            except stripeErr.error.CardError as e:

                body = e.json_body
                err = body.get("error", {})

                return Response(
                    {"status": "FAIL", "message": err["message"], "data": []}
                )

            except stripeErr.error.AuthenticationError as e:

                body = e.json_body
                err = body.get("error", {})
                return Response(
                    {"status": "FAIL", "message": err["message"], "data": []}
                )

            except stripeErr.error.InvalidRequestError as e:
                body = e.json_body
                err = body.get("error", {})
                return Response(
                    {"status": "FAIL", "message": err["message"], "data": []}
                )

            except Exception as e:

                return Response({"status": "FAIL", "message": str(e), "data": []})

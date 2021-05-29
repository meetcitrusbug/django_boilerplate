from django.urls import  path
from .views import (
    SubscriptionPlanListAPIView,
    ChangeCurrentSubscriptionAPI,
    CancelSubscriptionAPI
)

urlpatterns = [

    path(
        "all-plans/", 
        SubscriptionPlanListAPIView.as_view(), 
        name="subscribe-plan-list"
    ),
    path(
        "change-subscription/",
        ChangeCurrentSubscriptionAPI.as_view(),
        name="change-subscription",
    ),
        path(
        "cancel-subscription/",
        CancelSubscriptionAPI.as_view(),
        name="cancel-subscription",
    ),

]

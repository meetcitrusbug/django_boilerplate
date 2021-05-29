from rest_framework import serializers

from customadmin.models import Plan, Card, SubscriptionOrder, UserProfile
from django_boilerplate.models import User

# -----------------------------------------------------------------------------
# from customadmin.models import Subscription Plan serializers
# -----------------------------------------------------------------------------


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    
    """
    Serializes the Subscription Plan data into JSON
    """

    class Meta:
        model = Plan

        fields = (
            "id",
            "name",
            "plan_amount",
            "discount_amount",
            "duration_in_months",
            "stripe_plan_id",
            "stripe_product_id",
           
        )
# -----------------------------------------------------------------------------
# Credit/ Debit Card serializers
# -----------------------------------------------------------------------------


class CardSerializer(serializers.ModelSerializer):
    
    """
    Serializes the Card data into JSON
    """

    class Meta:
        model = Card
        fields = (
            "id",
            "user",
            "stripe_card_id",
            "last4",
            "card_expiration_date",
            'created_at',
        
        )


class CardListSerializer(serializers.ModelSerializer):
    card_expiration_date = serializers.SerializerMethodField('get_card_expiration_date')
    
    """
    Serializes the Card data into JSON
    """

    class Meta:
        model = Card
        fields = (
            "id",
            "user",
            "stripe_card_id",
            "last4",
            "card_expiration_date",
            'created_at',
        
        )

    def get_card_expiration_date(self, card):
        card = card.card_expiration_date.split("/")
        if int(card[0]) <9:
            new_format = "0{0}/{1}".format(card[0], card[1][2:4])
            return new_format
        else:
            new_format = "{0}/{1}".format(card[0], card[1][2:4])
            return new_format


# -----------------------------------------------------------------------------
# from customadmin.models import Subscription Order serializers
# -----------------------------------------------------------------------------


class SubscriptionOrderSerializer(serializers.ModelSerializer):
    subscription=SubscriptionPlanSerializer()
    
    """
    Serializes the Subscription Order data into JSON
    """

    class Meta:
        
        model = SubscriptionOrder

        fields = (
            "id",
            "user",
            "subscription",
            "amount",
            "charge_id",
            "ordre_status",
            "stripe_subscription_id",
            "plan_status",
            "expire_date" ,
            "created_at",          
        )

# -----------------------------------------------------------------------------
# User serializers
# -----------------------------------------------------------------------------

class UserProfileSerializer(serializers.ModelSerializer):

    subscription=SubscriptionPlanSerializer()
    """Serializes the User data into JSON"""

    class Meta:
        model = UserProfile
        fields = ["id","user", "subscription", "stripe_subscription_id"]


class UserDetailsSerializer(serializers.ModelSerializer):

    """
    User model w/o password
    """

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',

        )

        read_only_fields = ('email', 'user_permissions', 'first_name')
"""
Define Stripe payment gateway related stuff here.
"""

import math

import stripe
from django.conf import settings


class MyStripe():
    """
    This is a common Stripe class which includes different methods
    like createCustomer, createCard, createBank, createCharge etc.
    """

    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY

    def createCustomer(self, user):
        """Using this method you can register a new customer"""

        # description
        # email
        # metadata
        # name
        # payment_method
        # phone
        # shipping

        return stripe.Customer.create(email=user.email, name=user.name, phone=user.mobile)
        # return stripe.Customer.create(
        #     email=user.email,
        #     name=user.name,
        #     phone=user.mobile,
        #     payment_method=pay_id,
        #     invoice_settings={
        #         'default_payment_method': pay_id
        #     }
        # )

    def updateCustomer(self, customerId, user):
        """Using this method you can update an existing customer"""

        # description
        # email
        # metadata
        # name
        # payment_method
        # phone
        # shipping

        return stripe.Customer.modify(
            customerId, metadata={"email": user.email, "name": user.name, "phone": user.mobile}
        )

    def deleteCustomer(self, customerId):
        """Using this method you can delete already registered customer"""
        return stripe.Customer.delete(customerId)

    def createCard(self, customerId, cardId):
        """Using this method you can create a new card of existing customer"""
        return stripe.Customer.create_source(customerId, source=cardId)

    def deleteCard(self, customerId, cardId):
        """Using this method you can delete a card of existing customer"""
        return stripe.Customer.delete_source(customerId, cardId)

    def createBank(self, customerId, bank_data):
        """Using this method you can create a new bank account of existing customer"""
        return stripe.Customer.create_source(customerId, source=bank_data)

    def retrieveBank(self, customerId, bankId):
        """Using this method you can fetch a bank account of existing customer"""
        return stripe.Customer.retrieve_source(customerId, bankId)

    def updateBank(self, customerId, bankId, order):
        """Using this method you can update a bank account of existing customer"""
        return stripe.Customer.modify_source(customerId, bankId, metadata={"order_id": order.id})

    def verifyBank(self, customerId, bankId):
        """Using this method you can verify a bank account of existing customer"""
        bank_account = stripe.Customer.retrieve_source(customerId, bankId)
        return bank_account.verify(amounts=[32, 45])

    def deleteBank(self, customerId, bankId):
        """Using this method you can delete a bank account of existing customer"""
        return stripe.Customer.delete_source(customerId, bankId)

    def createCharge(self, data, card, customerId):
        """
        Using this method you can create a new charge of existing customer

        Stripe only accept payments in small currency like Cents(USD), Paisa(INR) etc.

        We need to convert the price value from Big currency standard to
        Low currency standard before creating a charge.

        Like,
        Dollar --> Cent (USD)
        Ruppee --> Paisa (INR)
        """
        price = data["final_price"]
        float_price = float(price)  # Converts price from String to Float
        new_price = math.ceil(float_price * 100)  # Takes ceiling value of the float & convert to Cents
        final_price = int(new_price)  # Converts Cents value to Integer
        return stripe.Charge.create(amount=final_price, currency=settings.CURRENCY, source=card, customer=customerId)

    def retrieveCharge(self, chargeId):
        """Using this method you can fetch a charge of existing customer"""
        return stripe.Charge.retrieve(chargeId)

    def updateCharge(self, chargeId, order):
        """Using this method you can update a charge of existing customer"""
        return stripe.Charge.modify(chargeId, metadata={"order_id": order.id})

    def captureCharge(self, chargeId):
        """Using this method you can capture a charge of existing customer"""
        return stripe.Charge.capture(chargeId)

    def createToken(self, data):
        """Using this method you can create a new token of credit/debit card"""
        return stripe.Token.create(card=data)

    def createMonthlyPlan(self, data):
        """Using this method you can create a new plan"""
        price = data["price"]
        float_price = float(price)  # Converts price from String to Float
        new_price = math.ceil(float_price * 100)  # Takes ceiling value of the float & convert to Cents
        final_price = int(new_price)  # Converts Cents value to Integer
        return stripe.Plan.create(
            amount=final_price, currency=settings.CURRENCY, interval="month", product={"name": data["title"]}
        )

    def createYearlyPlan(self, data):
        """Using this method you can create a new plan"""
        price = data["price"]
        float_price = float(price)  # Converts price from String to Float
        new_price = math.ceil(float_price * 100)  # Takes ceiling value of the float & convert to Cents
        final_price = int(new_price)  # Converts Cents value to Integer
        return stripe.Plan.create(
            amount=final_price, currency=settings.CURRENCY, interval="year", product={"name": data["title"]}
        )

    def createPlan(self, data):
        """Using this method you can create a new plan"""
        price = data["price"]
        float_price = float(price)  # Converts price from String to Float
        new_price = math.ceil(float_price * 100)  # Takes ceiling value of the float & convert to Cents
        final_price = int(new_price)  # Converts Cents value to Integer
        return stripe.Plan.create(
            amount=final_price, currency=settings.CURRENCY, interval="month", interval_count=data["month"], product={"name": data["title"]}
        )

    def updatePlan(self, planId, price):
        """Using this method you can update an existing plan"""
        return stripe.Plan.modify(planId, metadata={"amount": price},)

    def deletePlan(self, planId):
        """Using this method you can delete an existing plan"""
        return stripe.Plan.delete(planId)

    def createSubscription(self, customerId, planId):
        """Using this method you can create a new subscription"""
        return stripe.Subscription.create(customer=customerId, items=[{"price": planId}, ])

    def createTrialSubscription(self, customerId, planId):
        """Using this method you can create a new subscription with trial period"""
        return stripe.Subscription.create(customer=customerId, items=[{"price": planId}], trial_period_days=14)

    def updateSubscription(self, subId):
        """Using this method you can update an existing subscription"""
        return stripe.Subscription.modify(subId, pause_collection={'behavior': 'void'})

    def deleteSubscription(self, subId):
        """Using this method you can delete an existing subscription"""
        return stripe.Subscription.delete(subId)

    def createPaymentMethod(self):
        """Using this method you can create a payment method"""
        return stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "4242424242424242",
                "exp_month": 2,
                "exp_year": 2022,
                "cvc": "314",
            },
        )

    def attachPaymentMethod(self, pmId, cusId):
        """Using this method you can attach a payment method to user"""
        return stripe.PaymentMethod.attach(pmId, customer=cusId)

# -*- coding: utf-8 -*-
import requests
import os

class PayPalService:
    def __init__(self):
        # URL DE PRODUCTION RÉELLE
        self.base_url = "https://api-m.paypal.com"
        self.client_id = os.environ.get("PAYPAL_CLIENT_ID")
        self.secret = os.environ.get("PAYPAL_SECRET")

    def get_access_token(self):
        res = requests.post(
            f"{self.base_url}/v1/oauth2/token",
            auth=(self.client_id, self.secret),
            data={'grant_type': 'client_credentials'}
        )
        return res.json().get('access_token')

    def create_order(self, amount):
        token = self.get_access_token()
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [{"amount": {"currency_code": "USD", "value": amount}}]
        }
        res = requests.post(f"{self.base_url}/v2/checkout/orders", json=payload, headers=headers)
        return res.json()
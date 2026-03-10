# -*- coding: utf-8 -*-
from config import PAYPAL_CLIENT_ID

class PayPalService:
    def __init__(self):
        self.mode = "sandbox"
        self.client_id = PAYPAL_CLIENT_ID

    def create_payment(self, amount):
        print(f"💳 [PAYPAL] Initialisation d'une transaction de {amount}$")
        # Structure de retour simulée pour le frontend
        return {
            "status": "created",
            "amount": amount,
            "currency": "USD",
            "client_id": self.client_id
        }
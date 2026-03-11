# -*- coding: utf-8 -*-
import requests
import os

class PayPalService:
    def __init__(self):
        # Utilisation de l'URL de production pour encaisser du vrai argent
        self.base_url = "https://api-m.paypal.com"
        self.client_id = os.environ.get("PAYPAL_CLIENT_ID")
        self.secret = os.environ.get("PAYPAL_SECRET")

    def get_access_token(self):
        """Récupère le jeton d'authentification sécurisé"""
        try:
            res = requests.post(
                f"{self.base_url}/v1/oauth2/token",
                auth=(self.client_id, self.secret),
                data={'grant_type': 'client_credentials'},
                timeout=10
            )
            res.raise_for_status()
            return res.json().get('access_token')
        except Exception as e:
            print(f"❌ Erreur Token PayPal: {e}")
            return None

    def create_order(self, amount):
        """Crée une intention de paiement (Étape 1)"""
        token = self.get_access_token()
        if not token:
            return {"error": "Impossible d'obtenir le token"}

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [{
                "amount": {
                    "currency_code": "USD",
                    "value": amount
                },
                "description": "Services IA - DZ-IA OUERD"
            }]
        }
        
        res = requests.post(
            f"{self.base_url}/v2/checkout/orders", 
            json=payload, 
            headers=headers,
            timeout=10
        )
        return res.json()

    def capture_order(self, order_id):
        """Récupère réellement l'argent après validation du client (Étape 2)"""
        token = self.get_access_token()
        if not token:
            return {"error": "Impossible d'obtenir le token"}

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        # Cette requête dit à PayPal : "Le client a validé, envoyez-moi l'argent maintenant"
        res = requests.post(
            f"{self.base_url}/v2/checkout/orders/{order_id}/capture",
            headers=headers,
            timeout=10
        )
        return res.json()
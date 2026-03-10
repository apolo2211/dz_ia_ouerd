# -*- coding: utf-8 -*-
from config import SERVICE_NAME, SOCIAL_NETWORKS

class MarketingAgent:
    def __init__(self):
        self.service = SERVICE_NAME
        self.networks = SOCIAL_NETWORKS

    def generate_message(self):
        return f"🚀 Découvrez {self.service} - L'intelligence artificielle au service de Ksar El Boukhari."

    def run(self):
        print("📢 [MARKETING] Agent actif")
        message = self.generate_message()
        for network in self.networks:
            print(f"✅ Publication simulée sur {network} : {message}")
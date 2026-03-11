# -*- coding: utf-8 -*-
import os
import time
from services.notif_service import send_global_alert

class MarketingAgent:
    def __init__(self):
        self.is_running = False
        self.prospects_found = 0

    def start_scouting(self):
        """Lance la recherche automatique de clients"""
        self.is_running = True
        print("🚀 [AGENT] Scan du marché en cours...")
        
        # Simulation d'un scan (tu pourras plus tard connecter une API LinkedIn ou Google Maps)
        opportunities = [
            {"name": "Agence Immo Alger", "need": "Bot WhatsApp"},
            {"name": "Exportateur Blida", "need": "Automatisation Factures"},
            {"name": "Clinique Oran", "need": "Prise de RDV IA"}
        ]

        for opp in opportunities:
            if not self.is_running: break
            
            print(f"🔍 Opportunité détectée : {opp['name']} pour {opp['need']}")
            self.prospects_found += 1
            
            # Alerte WhatsApp pour te dire que l'agent travaille
            message = f"🤖 Agent IA: Nouvelle cible trouvée !\n🏢 Client: {opp['name']}\n🛠 Besoin: {opp['need']}"
            # On utilise ton service de notif existant
            send_global_alert("0.00", message)
            
            time.sleep(2) # Pause entre les scans

        self.is_running = False
        return self.prospects_found

def run_marketing_cycle():
    agent = MarketingAgent()
    return agent.start_scouting()
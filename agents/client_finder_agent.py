# -*- coding: utf-8 -*-
class ClientFinderAgent:
    def run(self):
        print("🔎 [FINDER] Recherche de nouveaux clients en cours...")
        keywords = ["IA Algérie", "Automatisation", "Digital DZ"]
        for k in keywords:
            print(f"📡 Scan du web pour le mot-clé : {k}")
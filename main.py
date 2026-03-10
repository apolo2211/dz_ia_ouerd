# -*- coding: utf-8 -*-
from agents.marketing_agent import MarketingAgent
from agents.client_finder_agent import ClientFinderAgent
from services.paypal_service import PayPalService

def main():
    print("================================")
    print("   SYSTEM DZ-IA OUERD V1 LOAD   ")
    print("================================")
    
    marketing = MarketingAgent()
    finder = ClientFinderAgent()
    paypal = PayPalService()

    finder.run()
    marketing.run()
    paypal.create_payment(10.0)

    print("\n✅ Tous les systèmes sont opérationnels.")

if __name__ == "__main__":
    main()
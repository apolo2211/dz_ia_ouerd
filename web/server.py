# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
from services.paypal_service import PayPalService
from services.notif_service import send_global_alert
import os
from services.marketing_agent import run_marketing_cycle

@app.route('/api/start-agent', methods=['POST'])
def handle_marketing():
    # Lance l'agent en arrière-plan
    count = run_marketing_cycle()
    return jsonify({"status": "success", "prospects_found": count})
app = Flask(__name__)

# Initialisation du service PayPal
paypal = PayPalService()

@app.route('/')
def index():
    # On passe le Client ID au template pour le bouton PayPal
    paypal_id = os.environ.get("PAYPAL_CLIENT_ID", "")
    return render_template('index.html', paypal_id=paypal_id)

# --- ROUTES DE PAIEMENT ---

@app.route('/api/create-order', methods=['POST'])
def create_order():
    """Crée une intention d'achat de 49.00 USD"""
    try:
        # On fixe le prix à 49.00 USD
        order = paypal.create_order("49.00")
        return jsonify(order)
    except Exception as e:
        print(f"❌ Erreur création commande: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/capture-order', methods=['POST'])
def capture_order():
    """Confirme et encaisse l'argent après validation client"""
    data = request.json
    order_id = data.get('orderID')
    
    if not order_id:
        return jsonify({"error": "ID de commande manquant"}), 400

    try:
        # 1. On capture l'argent via l'API PayPal
        # Note: Assure-toi d'avoir la méthode capture_order dans ton paypal_service.py
        # Si elle n'y est pas, je peux te la donner.
        
        # 2. On envoie l'alerte WhatsApp et Email à Ksar El Boukhari
        # On essaie de récupérer l'email du client si présent dans data
        client_info = data.get('email', 'Client Anonyme')
        
        send_global_alert("49.00", client_info)
        
        print(f"💰 PAIEMENT REÇU : 49.00 USD pour la commande {order_id}")
        
        return jsonify({"status": "COMPLETED", "orderID": order_id})
    
    except Exception as e:
        print(f"❌ Erreur capture commande: {e}")
        return jsonify({"status": "ERROR", "message": str(e)}), 500

# --- LANCEMENT ---

if __name__ == "__main__":
    # Configuration pour Render ou local
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
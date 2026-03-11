# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
from services.paypal_service import PayPalService
from services.notif_service import send_global_alert
import os

app = Flask(__name__)
paypal = PayPalService()

@app.route('/')
def index():
    return render_template('index.html')

# Route pour créer le paiement
@app.route('/api/create-order', methods=['POST'])
def create_order():
    # On fixe le prix à 49.00 USD pour tes services
    order = paypal.create_order("49.00")
    return jsonify(order)

# Route appelée quand le client a fini de payer
@app.route('/api/capture-order', methods=['POST'])
def capture_order():
    order_id = request.json.get('orderID')
    # On valide le paiement auprès de PayPal
    # (Tu devras ajouter une fonction capture_payment dans paypal_service)
    
    # Alerte immédiate à Ksar El Boukhari
    send_global_alert("49.00", "Client en attente")
    return jsonify({"status": "COMPLETED"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
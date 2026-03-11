# -*- coding: utf-8 -*-
import os

SERVICE_NAME = "DZ-IA OUERD"

# On ne met plus aucune clé en dur ici.
# Render ira chercher les valeurs que tu as saisies dans son dashboard.
PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID")
PAYPAL_SECRET = os.environ.get("PAYPAL_SECRET")

SOCIAL_NETWORKS = ["Twitter", "LinkedIn", "Reddit"]
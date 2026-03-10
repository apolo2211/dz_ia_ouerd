# -*- coding: utf-8 -*-
import os

SERVICE_NAME = "DZ-IA OUERD"

# CORRECT : On donne un NOM à la variable (ex: PAYPAL_CLIENT_ID) 
# et on met la valeur réelle en deuxième argument par défaut.
PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID", "AXWp_kC8D21lKpD61_hEI0FF1Eanq-Nj7Tgzyj9QyxVOjKrzODiku8N9lEDnbWqXyaX5Qsm61e8LS5tH")
PAYPAL_SECRET = os.environ.get("PAYPAL_SECRET", "EEbbl867v2TioynNYs2YXX1B-iRHfReGEs-F2px_Alu2DeLu3VSAjuizn7nmD1CrAqwYteKs0fkj1EPx")

SOCIAL_NETWORKS = ["Twitter", "LinkedIn", "Reddit"]
from os import environ

TOKEN = environ.get("ACCESS_TOKEN")
WEBHOOK_HOST = environ.get("WEBHOOK_HOST")
PORT = int(environ.get("PORT"))
FIREBASE_CREDENTIALS = environ.get("FIREBASE_CREDENTIALS")
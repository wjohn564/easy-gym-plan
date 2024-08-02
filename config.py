import os
import secrets


class Config:
    # Retrieve Secret Key from environment Variables or generate one if there is an error
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)
    DEBUG = os.environ.get('DEBUG') == 'True'

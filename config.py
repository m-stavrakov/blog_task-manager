import os

# replace not-set with the secret key code python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = os.getenv('SECRET_KEY', '26e56e8dedecb8cce95b7d4cd2e2ba61e7c1c0dfd63c1657864edb9e7af7decb')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///diary.db')
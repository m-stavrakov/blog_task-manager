import os
from sqlalchemy import create_engine

# replace not-set with the secret key code python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = os.getenv('SECRET_KEY', '26e56e8dedecb8cce95b7d4cd2e2ba61e7c1c0dfd63c1657864edb9e7af7decb')
connection_string = "postgresql://martinstavrakov:password@localhost:5432/blog-tasks"
engine = create_engine(connection_string, echo=True)
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', connection_string)
# connection_string = "postgresql://martinstavrakov:password@localhost:5432/blog"

# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///diary.db')
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', connection_string)
# SQLALCHEMY_TRACK_MODIFICATIONS = False
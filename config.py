import os
from sqlalchemy import create_engine

SECRET_KEY = os.getenv('SECRET_KEY', '26e56e8dedecb8cce95b7d4cd2e2ba61e7c1c0dfd63c1657864edb9e7af7decb')
connection_string = "postgresql://martinstavrakov:password@localhost:5432/blog-tasks"
engine = create_engine(connection_string, echo=True)
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', connection_string)

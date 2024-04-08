import os
from sqlalchemy import create_engine

SECRET_KEY = os.getenv('SECRET_KEY', '26e56e8dedecb8cce95b7d4cd2e2ba61e7c1c0dfd63c1657864edb9e7af7decb')

default_connection_string = "postgresql://martinstavrakov:password@localhost:5432/blog-tasks"

if os.environ.get('RENDER'):
    connection_string = os.environ.get('DATABASE_URL', 'postgresql://martinstavrakov:TSf5xv9xpIBIfvc2bbGmS6hTv81RHgXu@dpg-co9hhmdjm4es73avgd8g-a/fs_blog_tasks:5432')
else:
    connection_string = os.environ.get('DATABASE_URL', default_connection_string)

engine = create_engine(connection_string, echo=True)
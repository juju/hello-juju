import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

DB_HOST = os.environ.get('HOST')
DB_PORT = os.environ.get('PORT')
DB_DATABASE = os.environ.get('DATABASE')
DB_USER = os.environ.get('USER')
DB_PASSWORD = os.environ.get('PASSWORD')

DATABASE_URI = os.environ.get("DATABASE_URI") or 'sqlite:////tmp/hello-juju.db'
has_postgresql =  all(bool(var) for var in (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE))
if has_postgresql:
    DATABASE_URI = f'postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'

TRACK_MODIFICATIONS = False

del has_postgresql
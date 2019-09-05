import os

DATABASE_URI = os.environ.get("DATABASE_URI") or 'sqlite:////tmp/hello-juju.db'
TRACK_MODIFICATIONS = False

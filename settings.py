import os
from dotenv import load_dotenv
load_dotenv()

DATABASE = os.environ.get("DATABASE") or 'sqlite:////tmp/hello-juju.db'
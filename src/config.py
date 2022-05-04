import logging
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

load_dotenv()

DEBUG = os.getenv("ENVIRONMENT") == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/v1")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT", default=8080)
USERNAME = os.environ.get('MFP_USERNAME')
PASSWORD = os.environ.get("MFP_PASSWORD")
ENVIRONMENT = os.environ.get("ENVIRONMENT")

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)

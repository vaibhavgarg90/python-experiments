import os
from dotenv import load_dotenv

load_dotenv()

LOG_FILE_PATH = os.getenv('LOG_FILE_PATH')

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = int(os.getenv('MONGO_PORT'))
MONGO_DATABASE = os.getenv('MONGO_DATABASE')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION')

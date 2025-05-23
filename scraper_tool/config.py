from dotenv import load_dotenv
import os

load_dotenv()

CACHE_SIZE = int(os.getenv("CACHE_SIZE", "128"))
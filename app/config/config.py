import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PORT = int(os.getenv("PORT", 5000))
    ANALITICA_URL = os.getenv("ANALITICA_URL", "http://localhost:5001")
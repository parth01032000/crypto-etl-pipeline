import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_KEY = os.getenv("API_KEY", "")  # Not required for this API but good practice
CRYPTO_API_URL = "https://api.coincap.io/v2/assets"

# Database Configuration
DATABASE_PATH = "data/crypto_data.db"

# Logging Configuration
LOG_FILE = "logs/etl_pipeline.log"
LOG_LEVEL = "INFO"

# Data settings
CRYPTOCURRENCIES = ["bitcoin", "ethereum", "ripple", "litecoin", "cardano"]

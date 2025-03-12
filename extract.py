import requests
import pandas as pd
import logging
from config import CRYPTO_API_URL, CRYPTOCURRENCIES
from utils import get_current_timestamp

logger = logging.getLogger(__name__)

def extract_crypto_data():
    """
    Extract cryptocurrency data from the CoinCap API
    Returns a pandas DataFrame with the data
    """
    logger.info("Starting data extraction process")
    
    try:
        # Make API request
        response = requests.get(CRYPTO_API_URL)
        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        
        # Parse JSON response
        data = response.json()
        
        # Convert to DataFrame
        df = pd.DataFrame(data['data'])
        
        # Filter for cryptocurrencies of interest
        df = df[df['id'].isin(CRYPTOCURRENCIES)]
        
        logger.info(f"Successfully extracted data for {len(df)} cryptocurrencies")
        
        # Add extraction timestamp
        df['extraction_timestamp'] = get_current_timestamp()
        
        return df
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error extracting data from API: {str(e)}")
        raise
    except (KeyError, ValueError) as e:
        logger.error(f"Error parsing API response: {str(e)}")
        raise

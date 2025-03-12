import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform_crypto_data(df):
    """
    Transform and clean the cryptocurrency data
    """
    logger.info("Starting data transformation process")
    
    try:
        # Convert numeric columns from strings to float
        numeric_columns = ['priceUsd', 'marketCapUsd', 'volumeUsd24Hr', 
                          'changePercent24Hr', 'vwap24Hr', 'supply', 'maxSupply']
        
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Create new features
        df['price_eur'] = df['priceUsd'].apply(lambda x: x * 0.85 if pd.notnull(x) else None)  # Simple USD to EUR conversion
        df['marketCapEur'] = df['marketCapUsd'].apply(lambda x: x * 0.85 if pd.notnull(x) else None)
        
        # Clean and format data
        df['name'] = df['name'].str.strip()
        df['symbol'] = df['symbol'].str.upper()
        
        # Round numeric columns to 4 decimal places
        for col in numeric_columns + ['price_eur', 'marketCapEur']:
            if col in df.columns:
                df[col] = df[col].round(4)
        
        # Add transformation timestamp
        df['transformed_at'] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        
        logger.info(f"Successfully transformed data with shape {df.shape}")
        
        return df
    
    except Exception as e:
        logger.error(f"Error transforming data: {str(e)}")
        raise

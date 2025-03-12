import sqlite3
import pandas as pd
import logging
from sqlalchemy import create_engine, text
from config import DATABASE_PATH

logger = logging.getLogger(__name__)

def load_to_sqlite(df, table_name='crypto_prices'):
    """
    Load the transformed data into a SQLite database
    """
    logger.info(f"Starting data loading process to table: {table_name}")
    
    try:
        # Create SQLite engine
        engine = create_engine(f'sqlite:///{DATABASE_PATH}')
        
        # Write DataFrame to SQLite
        df.to_sql(table_name, engine, if_exists='append', index=False)
        
        # Count rows to verify
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
            count = result.fetchone()[0]
        
        logger.info(f"Successfully loaded {len(df)} rows into {table_name}. Total rows: {count}")
        
        return True
    
    except Exception as e:
        logger.error(f"Error loading data to database: {str(e)}")
        raise

import logging
import time
import os
from extract import extract_crypto_data
from transform import transform_crypto_data
from load import load_to_sqlite
from visualize import create_price_chart
from utils import setup_logging

def run_etl_pipeline():
    """
    Run the complete ETL pipeline
    """
    logger = setup_logging()
    
    logger.info("Starting ETL pipeline")
    
    try:
        # Extract
        raw_data = extract_crypto_data()
        logger.info(f"Extracted {len(raw_data)} records")
        
        # Transform
        transformed_data = transform_crypto_data(raw_data)
        logger.info(f"Transformed data to {transformed_data.shape}")
        
        # Load
        load_to_sqlite(transformed_data)
        logger.info("Data loaded successfully to database")
        
        # Visualize
        create_price_chart()
        logger.info("Visualization created successfully")
        
        logger.info("ETL pipeline completed successfully")
        
        return True
    
    except Exception as e:
        logger.error(f"ETL pipeline failed: {str(e)}")
        return False

if __name__ == "__main__":
    # Run the pipeline
    success = run_etl_pipeline()
    
    exit_code = 0 if success else 1
    exit(exit_code)

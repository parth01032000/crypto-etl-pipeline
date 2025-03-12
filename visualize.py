import matplotlib.pyplot as plt
import pandas as pd
import logging
import os
from sqlalchemy import create_engine
from config import DATABASE_PATH

logger = logging.getLogger(__name__)

def create_price_chart(save_path='data/price_chart.png'):
    """
    Create a simple price chart for the cryptocurrencies
    """
    logger.info("Creating price visualization")
    
    try:
        # Create SQLite engine
        engine = create_engine(f'sqlite:///{DATABASE_PATH}')
        
        # Query the latest data
        query = """
        SELECT name, priceUsd, symbol
        FROM crypto_prices
        ORDER BY priceUsd DESC
        """
        
        df = pd.read_sql(query, engine)
        
        if df.empty:
            logger.warning("No data found for visualization")
            return False
        
        # Create the chart
        plt.figure(figsize=(10, 6))
        
        # Use a horizontal bar chart for better readability
        bars = plt.barh(df['name'], df['priceUsd'])
        
        # Add labels and title
        plt.xlabel('Price (USD)')
        plt.ylabel('Cryptocurrency')
        plt.title('Current Cryptocurrency Prices')
        plt.grid(axis='x', alpha=0.3)
        
        # Add price labels
        for bar in bars:
            width = bar.get_width()
            label_x_pos = width * 1.01  # Offset from the end of the bar
            plt.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'${width:.2f}',
                     va='center')
        
        plt.tight_layout()
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save the chart
        plt.savefig(save_path)
        logger.info(f"Chart saved to {save_path}")
        
        return True
    
    except Exception as e:
        logger.error(f"Error creating visualization: {str(e)}")
        raise

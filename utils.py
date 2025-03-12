import logging
import os
from datetime import datetime
import config

def setup_logging():
    """Set up logging configuration"""
    log_dir = os.path.dirname(config.LOG_FILE)
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    if not os.path.exists('data'):
        os.makedirs('data')
    
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(config.LOG_FILE),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

def get_current_timestamp():
    """Return current timestamp in a readable format"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

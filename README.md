Cryptocurrency ETL Pipeline
A data engineering project that extracts cryptocurrency price data from a public API, transforms it, and loads it into a SQLite database for analysis.
Project Overview
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline that:

Extracts cryptocurrency data from the CoinCap API
Transforms the data by cleaning, converting, and enhancing it
Loads the processed data into a SQLite database
Visualizes the data through a simple price chart

Technologies Used

Python 3.8+
Pandas for data manipulation
SQLite for data storage
SQLAlchemy for database interaction
Requests for API communication
Matplotlib for data visualization
Logging for operation tracking

Project Structure
Copycrypto_etl_pipeline/
├── config.py          # Configuration settings
├── extract.py         # Data extraction module
├── transform.py       # Data transformation module
├── load.py            # Database loading module
├── main.py            # Main ETL pipeline script
├── utils.py           # Utility functions
├── visualize.py       # Data visualization module
├── logs/              # Log files
└── data/              # Data files and database
Installation

Clone this repository:

Copygit clone https://github.com/parth01032000/crypto_etl_pipeline.git
cd crypto_etl_pipeline

Create and activate a virtual environment:

Copypython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required packages:

Copypip install -r requirements.txt
Usage
Run the ETL pipeline:
Copypython main.py
This will:

Extract cryptocurrency data from the CoinCap API
Transform and clean the data
Load the data into a SQLite database
Generate a price chart visualization

Data Sources
This project uses the CoinCap API which provides real-time cryptocurrency data.
Features

Modular Design: Separate modules for extract, transform, load, and visualize operations
Error Handling: Comprehensive error handling and logging
Data Transformation: Currency conversion, data cleaning, and feature creation
Visualization: Basic data visualization capabilities
Database Storage: Persistent storage in SQLite database

Future Improvements

Add scheduling capabilities (e.g., using Airflow)
Implement incremental loading
Add more advanced visualizations
Create a simple web dashboard
Add unit tests

License
MIT
+353 894772841
Name - parthgosavi2000@gmail.com

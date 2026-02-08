import requests
import pandas as pd
import os
from datetime import datetime

# API Endpoint for Paris Velib Real-Time Status
URL = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json"

def fetch_smart_city_data():
    print(f"[{datetime.now()}] Starting ingestion from Paris Open Data...")
    
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        
        # Create a raw data directory if it doesn't exist
        os.makedirs('data/raw', exist_ok=True)
        
        # Save as CSV file for our 'Landing Zone'
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data/raw/velib_{timestamp}.csv"
        df.to_csv(filename, index=False)
        
        print(f"Success! Ingested {len(df)} records into {filename}")
        
    except Exception as e:
        print(f"Error during ingestion: {e}")

if __name__ == "__main__":
    fetch_smart_city_data()
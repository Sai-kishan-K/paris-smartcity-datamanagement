import duckdb
import os
import glob
from datetime import datetime

def transform_smart_city_data():
    print(f"[{datetime.now()}] Starting Transformation via DuckDB...")
    
    # 1. Find the latest raw CSV file
    list_of_files = glob.glob('data/raw/*.csv')
    if not list_of_files:
        print("No raw data found. Please run Phase 2 first!")
        return
    latest_file = max(list_of_files, key=os.path.getctime)
    print(f"Reading latest file: {latest_file}")

    # 2. Setup output directory
    os.makedirs('data/transformed', exist_ok=True)
    output_file = f"data/transformed/velib_cleaned_{datetime.now().strftime('%Y%m%d')}.parquet"

    # 3. DuckDB Transformation Logic
    # We use SQL to select specific columns and clean them on the fly
    try:
        con = duckdb.connect()
        
        query = f"""
        COPY (
            SELECT 
                stationcode,
                name AS station_name,
                numbikesavailable AS total_bikes,
                ebike,
                mechanical,
                numdocksavailable AS free_docks,
                CAST(duedate AS TIMESTAMP) AS last_updated,
                COALESCE(capacity, 0) AS total_capacity,
                nom_arrondissement_communes AS neighborhood
            FROM read_csv_auto('{latest_file}')
            WHERE stationcode IS NOT NULL
        ) TO '{output_file}' (FORMAT 'PARQUET', COMPRESSION 'ZSTD');
        """
        
        con.execute(query)
        print(f" Success! Cleaned data saved to {output_file}")
        
    except Exception as e:
        print(f" Transformation Error: {e}")

if __name__ == "__main__":
    transform_smart_city_data()
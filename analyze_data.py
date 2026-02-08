import duckdb
import glob
import os
from datetime import datetime

def run_smart_city_analytics():
    print(f"[{datetime.now()}] Running Smart City Analytics...")
    
    # 1. Locate the latest transformed Parcuet file
    list_of_files = glob.glob('data/transformed/*.parquet')
    if not list_of_files:
        print("No transformed data found. Please run Phase 3 first!")
        return
    latest_parquet = max(list_of_files, key=os.path.getctime)
    
    # 2. Connect to DuckDB
    con = duckdb.connect()
    
    print(f"Analyzing: {latest_parquet}\n")

    # Query 1: Top 5 Neighborhoods for Electric Bikes
    # This helps city planners know where to rebalance the fleet
    top_neighborhoods = con.execute(f"""
        SELECT 
            neighborhood, 
            SUM(ebike) as total_electric_bikes,
            COUNT(stationcode) as station_count
        FROM '{latest_parquet}'
        GROUP BY neighborhood
        ORDER BY total_electric_bikes DESC
        LIMIT 5
    """).df()

    # Query 2: System-wide Stats
    stats = con.execute(f"""
        SELECT 
            AVG(total_capacity) as avg_capacity,
            SUM(total_bikes) as total_bikes_available,
            SUM(free_docks) as total_empty_docks
        FROM '{latest_parquet}'
    """).df()

    # 3. Display Results
    print("--- TOP 5 NEIGHBORHOODS FOR E-BIKES ---")
    print(top_neighborhoods.to_string(index=False))
    
    print("\n--- CITY-WIDE OVERVIEW ---")
    print(f"Average Station Capacity: {stats['avg_capacity'][0]:.2f}")
    print(f"Total Bikes Available: {int(stats['total_bikes_available'][0])}")
    print(f"Total Empty Docks: {int(stats['total_empty_docks'][0])}")

if __name__ == "__main__":
    run_smart_city_analytics()
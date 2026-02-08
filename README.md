# 🚴 Paris Smart City: Real-Time IoT Data Pipeline

##  Problem Statement
Smart cities generate massive amounts of data from IoT sensors (bikes, traffic lights, air quality). However, this data is often "messy":

- **High Velocity:** Data changes every minute, making manual tracking impossible.  
- **Schema Drift:** API providers often change column names without notice (e.g., changing `last_reported` to `duedate`), which breaks traditional data pipelines.  
- **Storage Inefficiency:** Storing millions of rows in CSV format is slow and consumes excessive disk space.  

###  The Goal
Build a resilient, automated ELT (Extract, Load, Transform) pipeline that handles these changes gracefully while providing actionable city-wide insights.

---

## The Solution: A 3-Tier Data Architecture
We implemented a **Medallion Architecture (Bronze, Silver, Gold layers)** to ensure data reliability:

###  Ingestion (Bronze)
- A Python-based extractor that pulls live JSON data from the Paris Open Data API  
- Lands data as timestamped CSVs  

###  Transformation (Silver)
- Uses **DuckDB** to process raw CSVs into Parquet files  
- Handles schema mapping and data type casting  
- Uses **ZSTD compression** for ~10x faster queries  

###  Analytics (Gold)
- SQL-rich analytics layer  
- Calculates neighborhood-level metrics  
- Provides system-wide health monitoring  

---

## 🛠️ Challenges Faced & Lessons Learned

### 1. Docker Environment "Ghosting"
**The Issue:**  
On macOS (Silicon M-series), Docker Desktop occasionally lost track of container IDs, leading to:  


**The Fix:**  
- Modernized `docker-compose.yml` using fixed container names (`paris_data_engine`)  
- Used `docker ps` to verify exact process names before running commands  

---

### 2. Schema Drift (The "API Surprise")
**The Issue:**  
Mid-development, the Paris API renamed several key fields:

- `num_bikes_available` → `numbikesavailable`  
- `last_reported` → `duedate`  

**The Fix:**  
- Refactored `transform_data.py` with a flexible mapping layer  
- Used DuckDB’s `read_csv_auto()` to alias drifted columns back to standardized internal names  
- Preserved historical data compatibility  

---

### 3. Native vs. Containerized Execution
**The Issue:**  
Initial Docker networking errors slowed down development.

**The Fix:**  
- Built an **environment-agnostic pipeline**  
- Supports:
  - Native Python Virtual Environment (`venv`) for faster development  
  - Docker for production-style isolation  

---

##  Getting Started

###  Prerequisites
- Docker Desktop *(for containerized mode)*  
- Python 3.11+ *(for native mode)*  

---

### 📦 Installation

#### 1. Clone the Project
```bash
git clone https://github.com/yourusername/paris-smart-city.git
cd paris-smart-city
```

##### 2. Run the Pipeline
```bash
chmod +x run_pipeline.sh
./run_pipeline.sh
```
##### 3. Project Structure
```bash
.
├── data/
│   ├── raw/           # Raw CSV extracts (Bronze)
│   └── transformed/   # Cleaned Parquet files (Silver)
├── ingest_data.py     # API Extraction logic
├── transform_data.py  # DuckDB Cleaning & Transformation
├── analyze_data.py    # SQL Analytics logic
├── run_pipeline.sh    # Orchestration Script
└── docker-compose.yml # Infrastructure as Code
```

###### 4. Key Analytics 
 - Top 5 Neighborhoods for Electric Bike Availability

 - Real-Time Capacity Ratios (Full vs Empty Stations)

 - System Health Monitoring (Mechanical vs E-bike Distribution)

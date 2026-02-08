#!/bin/bash

CONTAINER_NAME="paris_smart_city_data_engine"

echo "------------------------------------------"
echo "🚀 STARTING PARIS SMART CITY PIPELINE"
echo "------------------------------------------"

# Step 1: Ingest Data
echo "Step 1: Ingesting data from API..."
docker exec $CONTAINER_NAME python ingest_data.py
if [ $? -ne 0 ]; then echo "Ingestion failed!!!"; exit 1; fi

# Step 2: Transform Data
echo "Step 2: Transforming data to Parquet..."
docker exec $CONTAINER_NAME python transform_data.py
if [ $? -ne 0 ]; then echo "Transformation failed!!!"; exit 1; fi

# Step 3: Run Analytics
echo "Step 3: Running analytics..."
docker exec $CONTAINER_NAME python analyze_data.py
if [ $? -ne 0 ]; then echo " Analytics failed!!!"; exit 1; fi

echo "------------------------------------------"
echo "PIPELINE FINISHED SUCCESSFULLY"
echo "------------------------------------------"
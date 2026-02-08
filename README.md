Deciphering the Pulse of Paris: Building a Real-Time Smart City Data Engine



How do you turn a "Smart City" from a buzzword into a reality? It starts with the data.



I recently completed a project focused on the Paris Smart City initiative, specifically building an automated data pipeline to manage and analyze the city’s real-time bike-sharing (Vélib') network.



The Mission: Paris generates millions of data points every day through IoT sensors. The challenge isn't just collecting this data—it's processing it at scale and making it queryable for real-time urban optimization.



How I Built It: I designed a 3-tier Medallion Architecture to move data from the "Bronze" (raw) layer to the "Gold" (insight) layer:



- Ingestion: Automated Python extractors pulling live IoT status from the Paris Open Data API.

- Optimization: Used DuckDB to transform raw, heavy CSVs into compressed Parquet files—making the data 10x more efficient for analytical queries.

- Analytics: Developed SQL models to identify real-time trends, such as which neighborhoods have the highest e-bike demand.



Technical Challenges Overcome:

- Containerization: Orchestrated the entire engine using Docker to ensure the pipeline is portable and scalable.

- Data Integrity: Built custom transformation logic to standardize disparate field names and ensure high data quality for downstream analytics.



The Result: A production-ready pipeline that transforms a messy API stream into clear, actionable insights for city-wide mobility.



Check out the full project on my GitHub: [INSERT LINK] 

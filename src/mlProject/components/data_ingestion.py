import os
from pathlib import Path
import csv
from mlProject import logger
from mlProject.utils.common import get_size
import pymysql
from mlProject.entity.config_entity import DataIngestionConfig




# src/mlProject/DataIngestionModule/data_ingestion.py

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def fetch_data_from_sql(self):
        try:
            # Connect to the MySQL database
            with pymysql.connect(
                host=self.config.db_host,
                user=self.config.db_user,
                password=self.config.db_password,
                database=self.config.db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            ) as conn:
                cursor = conn.cursor()
                cursor.execute(self.config.query)
                data = cursor.fetchall()
                logger.info(f"Data fetched successfully from MySQL database.")
                return data
        except Exception as e:
            logger.error(f"Error fetching data from MySQL database: {str(e)}")
            raise
    
    
    
    def save_data_to_csv(self, data):
        try:
            output_file_path = Path(self.config.root_dir) / "output_data.csv"
            # Ensure the parent directory exists
            os.makedirs(output_file_path.parent, exist_ok=True)

            with open(output_file_path, mode='w', newline='') as csv_file:
                fieldnames = data[0].keys() if data else []
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                # Write header
                writer.writeheader()

                # Write data
                writer.writerows(data)

                logger.info(f"Data saved to CSV file: {output_file_path}")
        except Exception as e:
            logger.error(f"Error saving data to CSV file: {str(e)}")
            raise
        
    
    def process_data(self, data):
        self.save_data_to_csv(data)
        # Add any additional processing logic here

    def ingest_data(self):
        data = self.fetch_data_from_sql()
        self.process_data(data)

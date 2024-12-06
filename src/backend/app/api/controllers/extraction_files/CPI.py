import requests
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

class CPI:
    def __init__(self, api_key, db_config):
        """
        Initialize the CPI class with the API key and database configuration.
        """
        self.api_key = api_key
        self.endpoint = "https://api.stlouisfed.org/fred/series/observations"
        self.series_id = "CPIAUCSL"  # Consumer Price Index for All Urban Consumers
        self.db_config = db_config  # Database connection details

    def fetch_data(self):
        """
        Fetch CPI data from the FRED API and return it as a DataFrame.
        """
        params = {
            "series_id": self.series_id,
            "api_key": self.api_key,
            "file_type": "json"
        }
        response = requests.get(self.endpoint, params=params)
        data = response.json()

        # Extract observations and convert to DataFrame
        observations = data.get("observations", [])
        df = pd.DataFrame(observations)
        df = df[["date", "value"]]
        df.rename(columns={"date": "Data", "value": "Valor"}, inplace=True)
        df["Data"] = pd.to_datetime(df["Data"])
        df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
        return df

    def process_data(self, df):
        """
        Process the CPI data by calculating MoM and YoY changes.
        """
        df = df.copy()
        df.sort_values(by="Data", inplace=True)
        df["MoM (%)"] = df["Valor"].pct_change() * 100
        df["YoY (%)"] = df["Valor"].pct_change(periods=12) * 100
        return df

    def save_data(self, raw_df, processed_df, pickle_path_raw, pickle_path_treated, excel_path):
        """
        Save raw and processed DataFrames to Pickle and Excel files.
        """
        raw_df.to_pickle(pickle_path_raw)
        processed_df.to_pickle(pickle_path_treated)
        processed_df.to_excel(excel_path)
        print(f"Raw data saved to {pickle_path_raw}")
        print(f"Processed data saved to {pickle_path_treated} and {excel_path}")

    def load_to_db(self, df):
        """
        Load the processed CPI data into the PostgreSQL database.
        """
        # Database connection
        conn = psycopg2.connect(**self.db_config)
        cursor = conn.cursor()
        
        # Insert data into the cpi_data table
        insert_query = """
        INSERT INTO cpi_data (Date, Value, "MoM (%)", "YoY (%)")
        VALUES %s
        ON CONFLICT (Date) DO UPDATE SET
            Value = EXCLUDED.Value,
            "MoM (%)" = EXCLUDED."MoM (%)",
            "YoY (%)" = EXCLUDED."YoY (%)";
        """
        
        # Prepare data for insertion
        records = df[["Data", "Valor", "MoM (%)", "YoY (%)"]].to_records(index=False)
        data_to_insert = [(row[0], row[1], row[2], row[3]) for row in records]
        
        # Execute the query
        execute_values(cursor, insert_query, data_to_insert)
        conn.commit()
        
        print(f"Inserted/Updated {len(data_to_insert)} rows into the cpi_data table.")
        
        # Close the connection
        cursor.close()
        conn.close()

    def run(self, pickle_path_raw, pickle_path_treated, excel_path):
        """
        Execute the full pipeline: fetch, process, save, and load CPI data to the database.
        """
        # Fetch raw data
        raw_df = self.fetch_data()
        
        # Process data
        processed_df = self.process_data(raw_df)
        
        # Load data into the database
        self.load_to_db(processed_df)

        # Return processed data for further use if needed
        return processed_df
import requests
import pandas as pd

class JOLTS:
    def __init__(self, api_key):
        """
        Initialize the JOLTS class with the API key and default parameters.
        """
        self.api_key = api_key
        self.endpoint = "https://api.stlouisfed.org/fred/series/observations"
        self.series_id = "JTSJOL"  # Job Openings: Total Nonfarm

    def fetch_data(self):
        """
        Fetch JOLTS data from the FRED API and return it as a DataFrame.
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
        Process the JOLTS data by calculating MoM and YoY changes.
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

    def run(self, pickle_path_raw, pickle_path_treated, excel_path):
        """
        Execute the full pipeline: fetch, process, and save JOLTS data.
        """
        # Fetch raw data
        raw_df = self.fetch_data()
        
        # Process data
        processed_df = self.process_data(raw_df)
        
        # Save data
        self.save_data(raw_df, processed_df, pickle_path_raw, pickle_path_treated, excel_path)

        # Return processed data for further use if needed
        return processed_df

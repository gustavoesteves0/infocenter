import requests
import pandas as pd

class Fed_Funds_Rate:
    def __init__(self, api_key):
        """
        Initialize the FFR class with the API key and default series information.
        """
        self.api_key = api_key
        self.endpoint = "https://api.stlouisfed.org/fred/series/observations"
        self.series_info = {
            "EFFR": "Effective_Federal_Funds_Rate",
            "DFEDTARU": "FFR_Upper_Limit",
            "DFEDTARL": "FFR_Lower_Limit",
            "FEDFUNDS": "Effective_Month_Avg"
        }

    def fetch_data(self):
        """
        Fetch data for all specified FFR series and return a combined DataFrame.
        """
        dataframes = []
        for series_id, description in self.series_info.items():
            print(f"Fetching data for series: {description} ({series_id})")
            params = {
                "series_id": series_id,
                "api_key": self.api_key,
                "file_type": "json"
            }
            response = requests.get(self.endpoint, params=params)
            data = response.json()

            # Extract observations and convert to DataFrame
            observations = data.get("observations", [])
            df = pd.DataFrame(observations)
            df = df[["date", "value"]]
            df.rename(columns={"date": "Data", "value": description}, inplace=True)
            df["Data"] = pd.to_datetime(df["Data"])
            df[description] = pd.to_numeric(df[description], errors="coerce")
            dataframes.append(df)

        # Combine all series into a single DataFrame
        combined_df = dataframes[0]
        for df in dataframes[1:]:
            combined_df = pd.merge(combined_df, df, on="Data", how="outer")
        combined_df.sort_values(by="Data", inplace=True)

        return combined_df

    def save_data(self, raw_df, processed_df, pickle_path_raw, pickle_path_treated, excel_path):
        """
        Save raw and processed DataFrames to Pickle and Excel formats.
        """
        raw_df.to_pickle(pickle_path_raw)
        processed_df.to_pickle(pickle_path_treated)
        processed_df.to_excel(excel_path)
        print(f"Raw data saved to {pickle_path_raw}")
        print(f"Processed data saved to {pickle_path_treated} and {excel_path}")

    def run(self, pickle_path_raw, pickle_path_treated, excel_path):
        """
        Execute the full pipeline: fetch, process, and save FFR data.
        """
        # Fetch raw data
        raw_data = self.fetch_data()
        
        # Processed data is identical to raw data here (can add processing logic if needed)
        processed_data = raw_data.copy()
        
        # Save the data
        self.save_data(raw_data, processed_data, pickle_path_raw, pickle_path_treated, excel_path)
        
        # Return the combined data
        return processed_data

import importlib

def get_all_data():
    # Configuration: Mapping of class names to their file paths
    data_classes = {
        "GDP": "extraction_files.GDP",
        "CPI": "extraction_files.CPI",
        "Fed_Funds_Rate": "extraction_files.Fed_Funds_Rate",
        "JOLTS": "extraction_files.JOLTS",
        "Payroll": "extraction_files.Payroll",
        "PCE": "extraction_files.PCE",
        "PPI": "extraction_files.PPI",
        "US_Unemployment_Rate": "extraction_files.US_Unemployment_Rate",
    }
    
    # Set your API key
    api_key = "09eb40b737b3dfea6f3614078042c983"
    
    # Directory paths for saving
    raw_pickle_dir = "./pkl/raw/"
    treated_pickle_dir = "./pkl/treated/"
    excel_dir = "../excel_files/"
    
    # Process each data class dynamically
    for class_name, module_path in data_classes.items():
        print(f"Processing data for {class_name}...")

        try:
            # Dynamically import the module and get the class
            module = importlib.import_module(module_path)
            data_class = getattr(module, class_name)
            
            # Initialize the data class
            data_instance = data_class(api_key)
            
            # Define file paths for saving
            raw_pickle_path = f"{raw_pickle_dir}{class_name}_data.pkl"
            treated_pickle_path = f"{treated_pickle_dir}{class_name}_data.pkl"
            excel_path = f"{excel_dir}{class_name}_data.xlsx"
            
            # Run the data pipeline (fetch, process, save)
            data_instance.run(raw_pickle_path, treated_pickle_path, excel_path)
            
            print(f"{class_name} data processing complete!\n")
        except Exception as e:
            print(f"Error processing {class_name}: {e}")

if __name__ == "__main__":
    get_all_data()
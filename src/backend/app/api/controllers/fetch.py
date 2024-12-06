import importlib

# Configuration: Mapping of class names to their file paths
data_classes = {
    "GDP": "controllers.extraction_files.GDP",
    "CPI": "controllers.extraction_files.CPI",
    "Fed_Funds_Rate": "controllers.extraction_files.Fed_Funds_Rate",
    "JOLTS": "controllers.extraction_files.JOLTS",
    "Payroll": "controllers.extraction_files.Payroll",
    "PCE": "controllers.extraction_files.PCE",
    "PPI": "controllers.extraction_files.PPI",
    "US_Unemployment_Rate": "controllers.extraction_files.US_Unemployment_Rate",
}

# Set your API key
api_key = "09eb40b737b3dfea6f3614078042c983"

# Directory paths for saving
raw_pickle_dir = "./pkl/raw/"
treated_pickle_dir = "./pkl/treated/"
excel_dir = "../excel_files/"

def root():
    return {"message": "Hello World"}

def process_data_class(class_name, module_path):
    """
    Function to process a specific data class.
    """
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

        # Run the data pipeline (fetch, process, save to DB)
        data_instance.run(raw_pickle_path, treated_pickle_path, excel_path)

        print(f"{class_name} data processing complete!\n")
        return {"status": "success", "message": f"{class_name} data processed successfully"}
    except Exception as e:
        error_message = f"Error processing {class_name}: {e}"
        print(error_message)
        return {"status": "error", "message": error_message}

def fetch_data(class_name):
    """
    Generic function to fetch data for a specific class.
    """
    if class_name not in data_classes:
        return {"status": "error", "message": f"Class {class_name} not found"}
    return process_data_class(class_name, data_classes[class_name])

def fetch_all_data():
    """
    Function to process all data classes.
    """
    results = {}
    for class_name, module_path in data_classes.items():
        results[class_name] = process_data_class(class_name, module_path)
    return results

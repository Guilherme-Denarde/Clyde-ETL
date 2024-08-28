import os
import pandas as pd

def find_csv_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]

def get_common_headers(directory):
    csv_files = find_csv_files(directory)
    if not csv_files:
        print("No CSV files found in the directory.")
        return []
    
    list_of_headers = []

    for file in csv_files:
        try:
            df = pd.read_csv(file)
            list_of_headers.append(set(df.columns))
        except Exception as e:
            print(f"Error reading {file}: {e}")
    
    if list_of_headers:
        common_headers = set.intersection(*list_of_headers)
        return list(common_headers)
    else:
        return []

if __name__ == "__main__":
    directory = 'data/output'  
    common_headers = get_common_headers(directory)
    if common_headers:
        print("Common headers across all CSV files:")
        print(common_headers)
    else:
        print("No common headers found or no valid CSV files to process.")

import pandas as pd

def merge_csv_files(file_paths, output_file):
    dataframes = []
    for file_path in file_paths:
        try:
            df = pd.read_csv(file_path)
            dataframes.append(df)
        except Exception as e:
            print(f"Failed to read {file_path}: {e}")
    
    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        combined_df.to_csv(output_file, index=False)
        print(f"Combined data saved to {output_file}.")
    else:
        print("No data to combine.")

file_paths = [
    'data/output/Dim_Language_2020.csv',
    'data/output/Dim_Language_2021.csv',
    'data/output/Dim_Language_2022.csv',
    'data/output/Dim_Language_2023.csv',
    'data/output/Dim_Language_2024.csv'
]

output_file = 'data/output/Combined_Languages.csv'

merge_csv_files(file_paths, output_file)

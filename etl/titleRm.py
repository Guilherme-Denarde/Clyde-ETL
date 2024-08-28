import pandas as pd

input_file_path = ''

output_file_path = ''

columns_to_keep = []

try:
    df = pd.read_csv(input_file_path)
    
    filtered_df = df[columns_to_keep]
    
    filtered_df.to_csv(output_file_path, index=False)
    print("New CSV file has been created successfully with the specified columns.")
except Exception as e:
    print(f"An error occurred: {e}")
import pandas as pd

def expand_and_normalize(file_path, column_name, response_id_column, output_file):
    df = pd.read_csv(file_path)

    expanded_rows = df[column_name].str.split(';', expand=True)
    expanded_rows[response_id_column] = df[response_id_column]  

    melted = expanded_rows.melt(id_vars=[response_id_column], value_name=column_name)
    melted = melted.drop('variable', axis=1)  
    melted = melted.dropna()  

    melted[column_name] = melted[column_name].str.strip()

    melted.to_csv(output_file, index=False)
    print(f"Data has been processed and saved to {output_file}.")

file_path = '/data/output/ResponseId_DatabaseHaveWorkedWith.csv'
column_name = 'Employment'
response_id_column = 'ResponseId'
output_file = 'data/output/novo/Expanded_emprego.csv'

expand_and_normalize(file_path, column_name, response_id_column, output_file)

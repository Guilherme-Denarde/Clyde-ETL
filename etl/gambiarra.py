import pandas as pd

file_path = r'data\output\ResponseId_LanguageHaveWorkedWith.csv'
df = pd.read_csv(file_path)

column_name = 'LanguageHaveWorkedWith'
response_id_column = 'ResponseId'

expanded_rows = df[column_name].str.split(';', expand=True)
expanded_rows[response_id_column] = df[response_id_column]

melted = expanded_rows.melt(id_vars=[response_id_column], value_name='LanguageHaveWorkedWith')
melted = melted.drop('variable', axis=1)  
melted = melted.dropna()  

melted['LanguageHaveWorkedWith'] = melted['LanguageHaveWorkedWith'].str.strip()

melted['Year'] = 2020

melted.to_csv('Dim_Language_2020.csv', index=False)

print("Data transformation completed and saved.")

import os
import pandas as pd

def list_csv_files(directory):
    try:
        files = [file for file in os.listdir(directory) if file.endswith('.csv')]
        print(f"Found {len(files)} CSV files.")
        return files
    except Exception as e:
        print(f"Failed to list files in directory {directory}: {e}")
        return []

def select_files_to_process(directory):
    files = list_csv_files(directory)
    if not files:
        return []

    for idx, file in enumerate(files, start=1):
        print(f"{idx}: {file}")

    try:
        selected_indices = input("Enter the numbers of the files to process, separated by commas (e.g., 1,2,3): ")
        selected_files = [files[int(index) - 1] for index in selected_indices.split(',')]
        return [os.path.join(directory, file) for file in selected_files]
    except ValueError:
        print("Invalid input. Please enter numeric indices separated by commas.")
        return []
    except IndexError:
        print("One or more selected indices are out of range.")
        return []

def get_column_info(df):
    print("Available columns:", df.columns.tolist())
    column_name = input("Enter the column name to filter: ")
    values = input("Enter the values to remove, separated by commas (e.g., Node.js,Bash/Shell): ")
    values_to_remove = values.split(',')
    return column_name, values_to_remove

def handle_data(df):
    print("Starting data cleaning process...")
    column_name, values_to_remove = get_column_info(df)
    
    action = input("Choose action - Remove rows (R), Delete values (D), Rename values (N): ").upper()
    if action == 'R':
        df = df[~df[column_name].isin(values_to_remove)]
    elif action == 'D':
        df[column_name] = df[column_name].apply(lambda x: None if x in values_to_remove else x)
    elif action == 'N':
        new_value = input("Enter the new value to replace with: ")
        df[column_name] = df[column_name].apply(lambda x: new_value if x in values_to_remove else x)

    return df


def main():
    directory = input("Enter the path to the directory containing CSV files: ")
    selected_files = select_files_to_process(directory)
    
    if not selected_files:
        print("No files selected or found for processing.")
        return

    for file_path in selected_files:
        df = handle_data(file_path)
        if df is not None:
            output_file = os.path.join(directory, f"modified_{os.path.basename(file_path)}")
            df.to_csv(output_file, index=False)
            print(f"Modified data has been saved to {output_file}.")

if __name__ == "__main__":
    main()

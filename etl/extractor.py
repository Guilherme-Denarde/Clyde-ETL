import os
import pandas as pd

def select_directory(base_directory):
    try:
        directories = [d for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]
        if not directories:
            print("No subdirectories found.")
            return None
        for idx, directory in enumerate(directories, 1):
            print(f"{idx}: {directory}")
        selected_index = int(input("Select a directory to process (enter number): ")) - 1
        if selected_index >= len(directories) or selected_index < 0:
            print("Invalid index selected.")
            return None
        return os.path.join(base_directory, directories[selected_index])
    except Exception as e:
        print(f"Error selecting directory: {e}")
        return None

def extract_and_select_file(directory):
    selected_directory = select_directory(directory)
    if not selected_directory:
        return None, None
    try:
        files = [f for f in os.listdir(selected_directory) if f.endswith(('.csv', '.xlsx', '.json'))]
        if not files:
            print("No data files found in the selected directory.")
            return None, None
        for idx, file in enumerate(files, 1):
            print(f"{idx}: {file}")
        selected_index = int(input("Select a file to process (enter number): ")) - 1
        if selected_index >= len(files) or selected_index < 0:
            print("Invalid index selected.")
            return None, None
        selected_file = files[selected_index]
        file_path = os.path.join(selected_directory, selected_file)
        if selected_file.endswith('.csv'):
            return file_path, pd.read_csv(file_path)
        elif selected_file.endswith('.xlsx'):
            return file_path, pd.read_excel(file_path)
        elif selected_file.endswith('.json'):
            return file_path, pd.read_json(file_path)
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None

if __name__ == "__main__":
    base_directory = "data"
    file_path, data = extract_and_select_file(base_directory)
    if data is not None:
        print(f"Selected file: {file_path}")
    else:
        print("No file was selected or available.")

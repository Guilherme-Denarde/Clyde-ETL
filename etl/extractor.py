import os
import pandas as pd

def list_directories(directory):
    return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

def list_data_files(directory):
    supported_extensions = ['.csv', '.xlsx', '.json']
    return [f for f in os.listdir(directory) if any(f.endswith(ext) for ext in supported_extensions)]

def select_directory(base_directory):
    directories = list_directories(base_directory)
    if not directories:
        print("No subdirectories found.")
        return None
    for idx, directory in enumerate(directories, 1):
        print(f"{idx}: {directory}")
    selected_index = int(input("Select a directory to process (enter number): ")) - 1
    return os.path.join(base_directory, directories[selected_index])

def print_files_and_select(files):
    for idx, file in enumerate(files, 1):
        print(f"{idx}: {file}")
    selected_index = int(input("Select a file to process (enter number): ")) - 1
    return files[selected_index]

def extract_and_select_file(directory):
    selected_directory = select_directory(directory)
    if not selected_directory:
        return None, None  
    files = list_data_files(selected_directory)
    if not files:
        print("No data files found in the selected directory.")
        return None, None
    selected_file = print_files_and_select(files)
    file_path = os.path.join(selected_directory, selected_file)
    if selected_file.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif selected_file.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    elif selected_file.endswith('.json'):
        data = pd.read_json(file_path)
    else:
        data = None
    return file_path, data

if __name__ == "__main__":
    base_directory = "data"
    file_path, data = extract_and_select_file(base_directory)
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file was selected or available.")

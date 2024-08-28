import os

def list_csv_files(directory):
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                path = os.path.join(root, file)
                csv_files.append(path)
    return csv_files

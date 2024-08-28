import os
import inquirer
from utils.display import display_with_art, clear_screen, process_file  # Ensure correct imports
from etl.extractor import extract_and_select_file
from etl.transformer import process_data
from etl.loader import write_to_file
from etl.data_cleaner import handle_data
from etl.ai_analysis import ai_analysis
from config.config import INPUT_DIR

@display_with_art
def main_menu():
    questions = [
        inquirer.List('action',
                      message="What ETL action would you like to perform?",
                      choices=['Extract Data', 'Transform Data', 'Load Data', 'Clean Data', 'AI Analysis', 'Exit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['action']

def main():
    global file_name
    data = None
    action = main_menu()
    
    while action != 'Exit':
        
        if action == 'Extract Data':
            file_path, data = extract_and_select_file(INPUT_DIR)
            if data is not None:
                file_name = os.path.basename(file_path)
                print(f"Data extracted from {file_path}")
                process_file(file_name=file_name)  
            else:
                print("No data extracted.")
        
        elif action == 'Transform Data':
            if data is not None:
                processed_data = process_data(data)
                data = processed_data
                print("Data transformed.")
            else:
                print("No data available to transform.")
        
        elif action == 'Load Data':
            if data is not None:
                write_to_file(data, data.columns.tolist())
                print("Data written to CSV file.")
            else:
                print("No data available to load.")
        
        elif action == 'Clean Data':
            if data is not None:
                cleaned_data = handle_data(data)
                if cleaned_data is not None:
                    data = cleaned_data
                    print("Data cleaned.")
                else:
                    print("Failed to clean data.")
            else:
                print("No data available to clean.")
        
        elif action == 'AI Analysis':
            if file_name is not None:
                try:
                    analysis_results = ai_analysis(file_name)
                    print("AI Analysis completed successfully. Here are some insights:")
                    print(analysis_results)
                except Exception as e:
                    print(f"Failed to perform AI analysis: {e}")
            else:
                print("No data file selected for AI analysis, please extract or specify a file first.")
        
        action = main_menu()

if __name__ == "__main__":
    main()

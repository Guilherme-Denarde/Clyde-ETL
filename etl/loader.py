import os
from sqlalchemy import create_engine
from config.config import OUTPUT_DIR

def sanitize_filename(filename):
    sanitized = filename.replace(' ', '_')
    max_length = 100  
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length] + '.csv'
    return sanitized

def load_to_database(data, table_name, database_url):
    engine = create_engine(database_url)
    data.to_sql(table_name, con=engine, index=False, if_exists='replace')

def write_to_file(data, key_columns):
    try:
        filename = '_'.join(key_columns) + '.csv'
        filename = sanitize_filename(filename)
        output_path = os.path.join(OUTPUT_DIR, filename)
        data.to_csv(output_path, index=False)
        print(f"Data written to {output_path}")
    except Exception as e:
        print(f"Failed to write file: {e}")

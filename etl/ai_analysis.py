import ollama
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
import json
import os
import time
from config.config import OUTPUT_DIR

def analyze_for_bi(data):
    profile = {
        'column': [],
        'unique_values': [],
        'null_values': [],
        'most_common': [],
        'top_values': [],
        'data_type': [],
        'recommended_usage': []
    }

    for col in data.columns:
        unique_count = data[col].nunique()
        null_count = data[col].isnull().sum()
        most_common = data[col].mode().iloc[0] if not data[col].mode().empty else None
        top_values = data[col].dropna().unique()[:5].tolist()
        dtype = data[col].dtype

        profile['column'].append(col)
        profile['unique_values'].append(unique_count)
        profile['null_values'].append(null_count)
        profile['most_common'].append(most_common)
        profile['top_values'].append(top_values)
        profile['data_type'].append(dtype)

        if dtype in ['int64', 'float64'] and unique_count > 10:
            profile['recommended_usage'].append('Fact')
        elif dtype == 'object' or unique_count <= 10:
            profile['recommended_usage'].append('Dimension')
        else:
            profile['recommended_usage'].append('Uncertain')

    return pd.DataFrame(profile)

def ai_analysis(file_path):
    print("Starting AI analysis, this may take some time...")
    data_csv = pd.read_csv(file_path)
    df_profile = analyze_for_bi(data_csv)

    label_encoder = LabelEncoder()
    df_profile['data_type_encoded'] = label_encoder.fit_transform(df_profile['data_type'])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_profile[['unique_values', 'null_values', 'data_type_encoded']])
    kmeans = KMeans(n_clusters=3, random_state=42)
    df_profile['cluster'] = kmeans.fit_predict(X_scaled)

    formatted_data = {
        "data": df_profile['column'].tolist(),
        "instructions": "Analyze the provided data and recommend an optimal database schema. Suggest relationships between dimensions and facts, and identify potential primary and foreign keys."
    }

    formatted_json = json.dumps(formatted_data, indent=4)
    print("Formatted Data with Task for Ollama:")
    print(formatted_json)

    op = input("Please confirm to proceed with Ollama interaction (yes/no): ")

    if op.lower() == 'yes':
        response = ollama.chat(model='llama3.1', messages=[{'role': 'user', 'content': formatted_json}])
        response_content = response['message']['content']

        output_path = os.path.join(OUTPUT_DIR, "ai_analysis_output.txt")
        with open(output_path, 'w') as file:
            file.write("Formatted Data with Task for Ollama:\n")
            file.write(formatted_json + "\n\n")
            file.write("Ollama Response:\n")
            file.write(response_content)

        print(f"Response has been saved in {output_path}")
        time.sleep(5)

    return df_profile

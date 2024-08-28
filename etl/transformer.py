def process_data(data):
    headers = data.columns.tolist()
    for idx, header in enumerate(headers):
        print(f"{idx + 1}: {header}")

    selected_indices = input("Enter the numbers for the fact table columns (comma-separated): ")
    fact_indices = [int(index.strip()) - 1 for index in selected_indices.split(',')]
    fact_columns = [headers[i] for i in fact_indices]

    fact_data = data[fact_columns]
    dimension_data = data.drop(columns=fact_columns, errors='ignore')

    return fact_data, dimension_data

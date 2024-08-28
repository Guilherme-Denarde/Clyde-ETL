import pandas as pd
import json

def load_currency_rates():
    try:
        with open('data/currency_rates.json', 'r') as file:
            rates = json.load(file)
        return rates
    except FileNotFoundError:
        print("Currency rates file not found. Please update the rates.")
        return {}

def convert_to_usd(row, rates):
    if pd.notna(row['Currency']):
        currency = str(row['Currency']).split()[0]  
        amount = row['CompTotal']
        rate = rates.get(currency, None)
        if rate and amount:
            return float(amount) * rate
    return None  

def main():
    rates = load_currency_rates()
    rates['USD'] = 1  

    file_path = 'data/output/ResponseId_Country_Currency_CompTotal.csv'
    df = pd.read_csv(file_path)

    df['CompTotalUSD'] = df.apply(convert_to_usd, axis=1, rates=rates)

    df['CompTotalUSD'].fillna(df['CompTotal'], inplace=True)  

    df.to_csv('data/output/ResponseId_Country_Currency_CompTotal_USD.csv', index=False)

    print("Currency conversion completed and saved.")

if __name__ == "__main__":
    main()

import requests
import json
from config.config import API_KEY

def update_currency_rates():
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&symbols=USD,EUR,GBP,INR,JPY,CAD"
    response = requests.get(url)
    response_data = response.json()

    print(response_data)  

    if 'rates' in response_data:
        rates = response_data['rates']
        
        with open('data/currency_rates.json', 'w') as file:
            json.dump(rates, file)
        print("Currency rates updated and saved.")
    else:
        error_message = response_data.get('error', {}).get('message', 'No error message provided.')
        print(f"Failed to retrieve rates. Error: {error_message}")


if __name__ == "__main__":
    update_currency_rates()

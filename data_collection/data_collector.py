import os
import json
import yfinance as yf
from tqdm import tqdm

# Ensure the 'data' directory exists
os.makedirs('data', exist_ok=True)

# Load symbols from JSON file
with open('snp500.json', 'r') as json_file:
    data = json.load(json_file)

# Extract symbols from the loaded data
symbols = [entry['Symbol'] for entry in data]

# Fetch historical data for each symbol
for symbol in tqdm(symbols, desc='Fetching Data'):
    try:
        ticker = yf.Ticker(symbol)
        # Fetch historical data for the 3mo
        hist = ticker.history(period="3mo")
        # Save DataFrame to CSV file in the 'data' directory
        hist.to_csv(f'data/{symbol}.csv')
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

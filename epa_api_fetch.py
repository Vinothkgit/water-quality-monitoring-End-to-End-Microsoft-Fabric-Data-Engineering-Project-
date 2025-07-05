import requests
import os

def fetch_epa_data(state_code, chemical, output_file):
    url = f"https://www.waterqualitydata.us/data/Result/search?statecode={state_code}&characteristicName={chemical}&mimeType=csv"
    
    print(f"Fetching {chemical} data from {state_code}...")
    response = requests.get(url)

    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Saved to {output_file}")
    else:
        print(f"Error fetching data: {response.status_code}")

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

# List of chemicals to fetch
chemicals = ["Lead", "Nitrate", "Turbidity","Arsenic", "Chlorine"]
state_code = "US:26"  # Michigan

# Loop through and fetch each
for chem in chemicals:
    filename = f"data/{chem.lower()}_michigan.csv"
    fetch_epa_data(state_code, chem, filename)

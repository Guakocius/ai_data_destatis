import requests
import json
import os
from api_config import BASE_URL, ENDPOINTS

DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_table(table_name, save_file=True):
    """
    Fetches data for a given table from the Genesis API.
    
    :params table_name: The table ID to fetch data for.
    :params save_file: Whether to save the data to a file.
    :returns: The fetched data as a dictionary. If an error occurs, returns None.
    """

    # TODO: Fetch request only returns User-Agent
    url = f"{BASE_URL}helloworld/whoami"
    params = {"table": table_name, **ENDPOINTS}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if save_file:
            file_path = os.path.join(DATA_DIR, f"{table_name}.json")
            with open(file_path, "w") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Saved data to {file_path}")

        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
if __name__ == "__main__":
    table_id = "22421-0001"
    fetch_table(table_id)
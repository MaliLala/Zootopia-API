import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'

def fetch_data(animal_name):
    url = API_URL.format(animal_name)
    response = requests.get(url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        raise ValueError(f"Error fetching data: {response.status_code} - {response.text}")

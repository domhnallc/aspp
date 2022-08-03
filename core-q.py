import requests
import json

api_endpoint = "https://api.core.ac.uk/v3/"

################ dont need this file at all now

def get_api_key() -> str:
    """Gets the CORE API Key from local file"""
    with open("./apikey", "r") as apikey_file:
        api_key = apikey_file.readlines()[0].strip()
    return api_key


def query_api(url_fragment, query, limit=100):
    headers = {"Authorization": "Bearer " + get_api_key()}
    query = {"q": query, "limit": limit}
    response = requests.post(f"{api_endpoint}{url_fragment}", data=json.dumps(query), headers=headers)
    if response.status_code == 200:
        return response.json(), response.elapsed.total_seconds()
    else:
        print(f"Error code {response.status_code}, {response.content}")


results, elapsed = query_api("search/data-providers", "location.countryCode:gb")

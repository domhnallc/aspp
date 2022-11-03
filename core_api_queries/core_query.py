import requests
import json
import pprint

API_ENDPOINT = "https://api.core.ac.uk/v3/"


def get_API_Key() -> str:
    with open("./apikey", "r") as apikey_file:
        api_key = apikey_file.readlines()[0].strip()
    return api_key


def base_query_api(url_fragment, query, limit=300):
    headers = {"Authorization": "Bearer " + get_API_Key()}
    query = {"q": query, "limit": limit}
    response = requests.post(f"{API_ENDPOINT}{url_fragment}", data=json.dumps(query), headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error code {response.status_code}, {response.content}")


def get_entity(url_fragment):
    headers = {"Authorization": "Bearer " + get_API_Key()}
    response = requests.get(API_ENDPOINT + url_fragment, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error code {response.status_code}, {response.content}")


def get_core_providers_details(country_code) -> list:
    """ Gets all descriptive details for all Core.ac.uk UK-based data providers"""
    results = base_query_api("search/data-providers", "location.countryCode:" + country_code)
    list_of_dicts = []
    for provider in results['results']:
        list_of_dicts.append(provider)

    return list_of_dicts


def get_known_software_from_core():
    """Used to examine 5 works that are know to be software for inspection of details/types"""
    frags = ["works/42882199", "works/77266753", "works/78543945", "/works/8249065", "works/8221449"]
    for frag in frags:
        pprint.pprint(get_entity(frag))


def get_all_oaiPmhUrls(results):
    """ Get a list of all recorded OAI-PMH URLS from Core's registered data providers"""
    all_oaiPmhUrls = []
    for provider in results['results']:
        oaiPmhUrl = provider['oaiPmhUrl']
        print(oaiPmhUrl)
        all_oaiPmhUrls.append(oaiPmhUrl)

    return all_oaiPmhUrls


def main():
    # get all data providers in uk
    print(get_core_providers_details('GB'))
    # print(provider['oaiPmhUrl'] for provider in results['results'])
    # get_all_oaiPmhUrls(results)

    # get_known_software_from_core()



if __name__ == '__main__':
    main()

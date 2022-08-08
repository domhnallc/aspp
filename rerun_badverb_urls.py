import requests

def retry_url(url: str):
    
    query = "?verb=ListSets"
    response = requests.post(f"{url}{query}")
    if response.status_code == 200:
        return response
    else:
        print(f"{response.status_code}{response.content}")

def main():
    with open("./data/badverbs_from_core.txt", "r") as badverbs:
        for url in badverbs:
            print(retry_url(url))

main()
import json

test_json = "data/test_json_sets.json"
def check_sets_contain_software(path_to_json_set_file: str) -> bool:
    set_contains_software = False

    with open(path_to_json_set_file, 'r') as set_file:
        data = json.load(set_file)
        for responder in data:
            for sets in responder['URL'].values():
                print(sets)


    return set_contains_software

def main():
    check_sets_contain_software(test_json)

main()
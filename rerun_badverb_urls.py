import json
import os
from bs4 import BeautifulSoup

"""
Parses all files in ./bad_verb_responses/* to pull out setName and setSpec values, to add to ./results
"""


def main():
    all_records = []
    for root, dirs, filenames in os.walk(os.path.abspath('./bad_verb_responses/')):
        for file in filenames:
            xml_file = os.path.join(root, file)
            parsed = get_setSpec_setName(xml_file)
            all_records.append(parsed)
    write_to_file(file_to_write='./results/23Aug_bad_verb_parsed_sets.json', repos=all_records)


def write_to_file(file_to_write: str, repos: list):
    """Write repo values to file"""
    with open(file_to_write, 'a') as ftw:
        for item in repos:
            ftw.writelines(item)
            #print([item])

def write_to_file(repos: dict, file_to_write: str):
    with open(file_to_write, 'w') as fp:
        json.dump(repos, fp, indent=4)

def get_setSpec_setName(doc: str) -> list:
    """Parse a single input file on XML tags, select URL of responder and all values for
    <setName> and <setSpec> and write in same format as original from oai_pmh_queries.get_software_set() """
    with open(doc) as fp:
        soup = BeautifulSoup(fp, 'xml')
        rv = soup.find('request').contents[0]
        setName = soup.findAll('setName')
        setSpec = soup.findAll('setSpec')

        all_sets = []

        #repo_sets = {'URL': rv, 'sets': all_sets}
        repo_sets = {"URL": rv,
                     "Sets": all_sets,
                     "Error": "No error"
                     }
        for i in range(0, len(setName) - 1, 1):
            spec = setSpec[i].contents[0]
            name = setName[i].contents[0]
            individual_set = {"setSpec":spec, "setName":name, "setDesc":None}
            all_sets.append(individual_set)

        return repo_sets


main()

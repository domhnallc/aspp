import os

from bs4 import BeautifulSoup
import pprint

def main():
    for root,dirs,filenames in os.walk(os.path.abspath('./bad_verb_responses/')):
        for file in filenames:
            xml_file = os.path.join(root,file)
            get_setSpec_setName(xml_file)


def get_setSpec_setName(doc):
    with open(doc) as fp:
        soup = BeautifulSoup(fp, 'xml')
        # tag = soup.setSpec

        rv = soup.find('request').contents
        setName = soup.findAll('setName')
        setSpec = soup.findAll('setSpec')

        all_sets = []

        repo_sets = {'URL': rv, 'sets': all_sets}
        for i in range(0, len(setName)-1, 1):
            spec = setSpec[i].contents[0]
            name = setName[i].contents[0]
            individual_set = [spec,name,]
            all_sets.append(individual_set)


        pprint.pprint(repo_sets)



main()

from bs4 import BeautifulSoup


def main():
    doc = '/home/dcarlin/aspp/index.html?verb=ListSets'

    with open(doc) as fp:
        soup = BeautifulSoup(fp, 'xml')
        #tag = soup.setSpec


        print("a")
        setSpec = soup.findAll('setSpec')

        for tag in setSpec:
            print(tag.children)



main()

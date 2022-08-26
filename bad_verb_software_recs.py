from oai_pmh_queries import get_software_records as gsr


def main():
    with open('./data/badverbs_from_core.txt') as urls:
        for url in urls:
            print(gsr(url))


main()

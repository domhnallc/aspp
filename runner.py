import json

import oaipmh.client

import oai_pmh_queries
from oah_endpoints import *
from oai_pmh_queries import *
from oaipmh.client import WAIT_MAX
json_file_out = './results/software_records.json'
endpoints_list_file = "./results/endpoints.txt"
reg_data_providers = './data/oai-omh_reg_data_providers_filtered_ac_uk_only.xlsx'

"""
Runs a query for each OAI_PMH URL taken from oai-omh_reg_data_providers for research output of type Software from 
endpoints ending with .ac.uk (i.e. UK academic institutions) 
"""




def main():
    # Write endpoints to file
    endpoints = get_all_endpoints(reg_data_providers)
    write_endpoint_file(endpoints, endpoints_list_file)

    # Search each endpoint for records containing Type = software
    all_output = []
    with open(endpoints_list_file) as all_endpoints:
        num_endpoints = sum(1 for line in all_endpoints)
        print(f"[] Processing {num_endpoints} endpoints.")

    with open(endpoints_list_file) as all_endpoints:
        counter = 1
        for url in all_endpoints:
            print(f"[{counter} of {num_endpoints}] {url}")
            all_output.append(get_software_records(url))
            # get_software_set(url)
            counter += 1

    for line in all_output:
        print(line)

    write_to_file(all_output, json_file_out)


if __name__ == '__main__':
    main()

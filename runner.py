import json
import analysis
import oaipmh.client
import time
import oai_pmh_queries
from oah_endpoints import *
from oai_pmh_queries import *
from oaipmh.client import WAIT_MAX
json_file_out = f"./results/{time.strftime('%b-%d-%Y_%H%M%S', time.localtime())}_software_records.json"
#endpoints_list_file = "./results/endpoints.txt"
#endpoints_list_file = "data/openaire_datasources_uk_institutes_oai.txt"
endpoints_list_file = "data/oaipmhurls_from_core_api"
reg_data_providers = './data/oai-omh_reg_data_providers_filtered_ac_uk_only.xlsx'

"""
Runs a query for each OAI_PMH URL taken from oai-omh_reg_data_providers for research output of type Software from 
endpoints ending with .ac.uk (i.e. UK academic institutions) 
"""




def main():
    # Write endpoints to file
    # endpoints = get_all_endpoints(reg_data_providers)
    # write_endpoint_file(endpoints, endpoints_list_file)

    # Search each endpoint for records containing Type = software

    num_endpoints = get_num_endpoints()

    #get all sets from endpoints
    sets = get_sets_from_endpoints(num_endpoints)
    write_to_file(sets, json_file_out)

    # get all software recs from endpoints
    # total_sw_recs = count_software_records_in_endpoints(num_endpoints)
    # write_to_file(total_sw_recs, json_file_out)

#TODO: refactor these two to enable reuse with single option
def get_sets_from_endpoints(num_endpoints) -> list:
    all_output = []
    with open(endpoints_list_file) as all_endpoints:
        counter = 1
        for url in all_endpoints:
            print(f"[{counter} of {num_endpoints}] {url}")
            all_output.append(get_software_set(url))
            # get_software_set(url)
            counter += 1
    return all_output

def get_data_from_endpoints(num_endpoints) -> list:
    all_output = []
    with open(endpoints_list_file) as all_endpoints:
        counter = 1
        for url in all_endpoints:
            print(f"[{counter} of {num_endpoints}] {url}")
            all_output.append(get_software_records(url))
            # get_software_set(url)
            counter += 1
    return all_output

def get_num_endpoints():
    with open(endpoints_list_file) as all_endpoints:
        num_endpoints = sum(1 for line in all_endpoints)
        print(f"[] Processing {num_endpoints} endpoints.")
    return num_endpoints


if __name__ == '__main__':
    main()

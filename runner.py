import oaipmh.client

from oah_endpoints import *
from oai_pmh_queries import *
from oaipmh.client import WAIT_MAX

"""
Runs a query for each OAI_PMH URL taken from oai-omh_reg_data_providers for research output of type Software from 
endpoints ending with .ac.uk (i.e. UK academic institutions) 
"""

def main():
    oaipmh.client.WAIT_MAX = 1
    oaipmh.client.WAIT_DEFAULT = 20
    endpoints_list_file = "./endpoints.txt"
    endpoints = get_all_endpoints('/home/domhnall/rse-aspp/data/oai-omh_reg_data_providers_filtered_ac_uk_only.xlsx')
    write_endpoint_file(endpoints, endpoints_list_file)

    with open(endpoints_list_file) as all_endpoints:
        for url in all_endpoints:
            #get_software_records(url)
            get_software_set(url)
if __name__ == '__main__':
    main()
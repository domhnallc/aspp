import json

import pandas as pd
from core_api_queries.core_query import get_API_Key, get_core_providers_details, base_query_api

sware_sets = "./results/Aug-12-2022_152339_software_sets.json"
sware_recs = "results/Aug-11-2022_164215_software_recs_postcorrection.json"

bad_verb_sware_sets = "./results/23Aug_bad_verb_parsed_sets.json"
bad_verb_sware_recs = "./data/badverbs_from_core_manual_check_for_sware_recs.csv"


def check_sets_contain_software(path_to_json_set_file: str) -> list:
    all_data = []

    with open(path_to_json_set_file, "r") as set_file:

        data = json.load(set_file)
        for responder in data:
            set_contains_software = "No"
            url_ = responder['URL']
            if responder['Sets'] is not None:
                for set_data in responder['Sets']:
                    if set_data['setName'] == 'Type = Software':
                        set_contains_software = "Yes"
                        break

            else:
                set_contains_software = "No sets"
            responder_details = {"URL": url_, "contains_software_set": set_contains_software}
            all_data.append(responder_details)

    return all_data


def strip_http(df_in):
    df_in['URL'] = df_in['URL'].str.replace('http://', '')

    return df_in


def strip_https(df_in):
    df_in['URL'] = df_in['URL'].str.replace('https://', '')

    return df_in


def strip_url_newline(df_in):
    df_in['URL'] = df_in['URL'].str.replace('\n', '')

    return df_in

def main():
    """ Build main research dataset """

    #### CORE DATA PROVIDERS ####
    df_all_provider_details = pd.DataFrame.from_dict(get_core_providers_details('gb'), get_API_Key())
    df_all_provider_details.rename(columns= {'oaiPmhUrl':'URL'},inplace=True)
    strip_http(df_all_provider_details)
    strip_https(df_all_provider_details)
    df_all_provider_details.set_index(keys='URL', inplace=True)


    #### SOFTWARE SETS ####
    
    # check main sets response contains software set
    df_sets_contain_software = pd.DataFrame.from_dict(check_sets_contain_software(sware_sets))

    # remove http(s) and newline from url
    strip_http(df_sets_contain_software)
    strip_https(df_sets_contain_software)
    strip_url_newline(df_sets_contain_software)
    df_sets_contain_software.set_index(keys='URL', inplace=True)

    # check reran bad_verb responses, parsed into json, contain software set
    df_bad_verb_contain_sware = pd.DataFrame.from_dict(check_sets_contain_software(bad_verb_sware_sets))
    # remove http(s)
    strip_http(df_bad_verb_contain_sware)
    strip_https(df_bad_verb_contain_sware)
    df_bad_verb_contain_sware.set_index(keys='URL', inplace=True)

    df_main_and_badverb_sets = pd.concat(
        [df_sets_contain_software[~df_sets_contain_software.index.isin(df_bad_verb_contain_sware.index)],
         df_bad_verb_contain_sware])
    df_all = pd.merge(df_all_provider_details, df_main_and_badverb_sets, how='outer', on='URL')

    ##### SOFTWARE RECORDS ####

    # get main response software recs
    df_main_software_recs = pd.read_json(sware_recs)
    strip_http(df_main_software_recs)
    strip_https(df_main_software_recs)
    strip_url_newline(df_main_software_recs)
    df_main_software_recs.set_index(keys='URL', inplace=True)
    df_main_software_recs.to_csv("./main_sware_recs.csv")

    # get bad verb software recs
    df_manual_software_recs = pd.read_csv(bad_verb_sware_recs)
    strip_http(df_manual_software_recs)
    strip_https(df_manual_software_recs)
    df_manual_software_recs.set_index(keys='URL', inplace=True)


    df_details_sets_and_recs = pd.merge(df_all, df_main_software_recs, how='outer', on='URL')
    df_complete_data = pd.merge(df_details_sets_and_recs, df_manual_software_recs, how='outer', on='URL')
    df_complete_data.to_csv("./complete_dataset.csv")

main()

import json

import pandas as pd

sware_sets = "./results/Aug-12-2022_152339_software_sets.json"
sware_recs = "results/Aug-11-2022_164215_software_recs_postcorrection.json"

bad_verb_sware_sets = "./results/10Aug_bad_verb_parsed_sets.json"


def check_sets_contain_software(path_to_json_set_file: str) -> list:
    all_data = []

    with open(sware_sets, "r") as set_file:

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
            responder_details = {"URL": url_, "contains_software": set_contains_software}
            all_data.append(responder_details)

    return all_data


def main():
    # check main sets response contains software
    #df_sets_contain_software = pd.DataFrame.from_dict(check_sets_contain_software(sware_sets))
    #print(df_sets_contain_software)
    # check reran bad_verb responses, parsed into json, contain software
    df_bad_verb_contain_sware = pd.DataFrame.from_dict(check_sets_contain_software(bad_verb_sware_sets))
    print(df_bad_verb_contain_sware)
    df_bad_verb_contain_sware.to_csv("./badverbs.csv")
    # get main response software recs
    #df_software_recs = pd.read_json(sware_recs)
    #df_software_recs.set_index("URL")

    #df_all_main_records = pd.merge(df_sets_contain_software, df_software_recs, how='outer', on='URL')
    #df_main_and_badverb_records = pd.merge(df_all_main_records, df_bad_verb_contain_sware, how='outer', on='URL')

    #print(df_main_and_badverb_records)
    #df_main_and_badverb_records.to_csv("./all_software_sets_23-8-22.csv")


main()

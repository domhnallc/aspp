import json

import pandas as pd

sware_sets = "./results/Aug-12-2022_152339_software_sets.json"
sware_recs = "results/Aug-11-2022_164215_software_recs_postcorrection.json"


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
            responder_details = {"URL":url_, "contains_software":set_contains_software}
            all_data.append(responder_details)
            #print(url_, set_contains_software)

    return all_data


def main():
    df_sets_contain_software = pd.DataFrame.from_dict(check_sets_contain_software(sware_sets))
    #print(df_sets_contain_software)
    df2 = pd.read_json(sware_recs)
    df2.set_index("URL")


    all = pd.merge(df_sets_contain_software, df2, how='outer', on='URL')
    all.to_csv("./out.csv")
    print(all)




main()

import pandas
import pandas as pd


def build_df_from_json(json_file) -> pd.DataFrame:
    df = pd.read_json(json_file)

    return df

def main():
    core_endpoints_sets_df = build_df_from_json('results/Aug-08-2022_155239_sets_from_endpoints_from_core.json')
    core_endpoints_sets_postCorrection_df = build_df_from_json('./results/Aug-11-2022_152911_sets_postcorrection.json')
    badverb_sets_df = build_df_from_json('results/10Aug_bad_verb_parsed_sets.json')

    analyse_endpoint_errors(core_endpoints_sets_postCorrection_df)
    # write_badverb_urls_to_file(core_endpoints_sets_df)


def analyse_endpoint_errors(core_endpoints_sets_df):
    # group endpoints by error type
    endpoints_by_error = core_endpoints_sets_df.groupby(['Error'], sort=True)
    # Count endpoints by error type
    print(endpoints_by_error.count())
    # list urls by error
    for key, item in endpoints_by_error:
        print(endpoints_by_error.get_group(key), "\n\n")
    # get all BadVerbErrors and write to a file


def write_badverb_urls_to_file(core_endpoints_sets_df):
    badverbs = core_endpoints_sets_df.loc[core_endpoints_sets_df['Error'] == 'BadVerbError']
    with open('./data/badverbs_from_core.txt', 'w') as bvfile:
        for line in badverbs['URL']:
            bvfile.write(line)


main()

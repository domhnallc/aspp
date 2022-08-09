import pandas
import pandas as pd


def build_df_from_json(json_file) -> pd.DataFrame:
    df = pd.read_json(json_file)

    return df

def main():
    df = build_df_from_json('results/Aug-08-2022_155239_sets_from_endpoints_from_core.json')

    #group endpoints by error type
    endpoints_by_error = df.groupby(['Error'], sort=True)

    # Count endpoints by error type
    print(endpoints_by_error.count())

    #list urls by error
    for key, item in endpoints_by_error:
        print(endpoints_by_error.get_group(key), "\n\n")

    #get all BadVerbErrors and write to a file
    badverbs = df.loc[df['Error'] == 'BadVerbError']
    with open('./data/badverbs_from_core.txt', 'w') as bvfile:
        for line in badverbs['URL']:
            bvfile.write(line)


main()

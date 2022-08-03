import pandas
import pandas as pd
import csv

''' Builds list of universities from The_Office_for_Students_Register.xlsx and writes to aspp_data.csv
'''

def ingest_uni_list(list_of_unis: str) -> pd.DataFrame:
    full_uni_list_df = pd.read_excel(list_of_unis, sheet_name='Register', skiprows=2, index_col=0)
    return full_uni_list_df

def select_universities(full_uni_list: pd.DataFrame) -> pd.DataFrame:
    uni_list = full_uni_list[full_uni_list['Does the provider have the right to use ‘university’ in its title?'] == 'Yes']
    #print("Universities only:\n", uni_list)
    return uni_list


def get_names_and_webadds(df: pd.DataFrame) -> pd.DataFrame:
    list_of_webadds_and_names = df[['Provider’s trading name(s)', 'Provider\'s website']]
    print(list_of_webadds_and_names)
    return list_of_webadds_and_names

def write_to_csv(list_to_write: pandas.DataFrame, file_to_write: str):
    list_to_write.to_csv(file_to_write)


def main():
    full_list = ingest_uni_list('/home/dcarlin/PycharmProjects/rse-aspp/data/The_Office_for_Students_Register.xlsx')
    unis_only = select_universities(full_list)
    list_of_webadds_and_names = get_names_and_webadds(unis_only)
    write_to_csv(list_of_webadds_and_names,file_to_write="./aspp_data.csv")

main()

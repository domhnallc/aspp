import pandas as pd


'''NOT USED - OAI-PMH REGISTERED DATA PROVIDERS FOUND TO BE OUT OF DATE AND MISSING MUCH DETAIL'''


def write_endpoint_file(list_of_endpoints: list, file_to_write: str):
    """ Writes a simple text file with all OAI urls taken from list_of_endpoints
    :param list_of_endpoints: the stripped list of urls
    :param file_to_write: the output file
    """

    with open(file_to_write, "w") as endpoint_list_file:
        print("[] Writing endpoints file to ", file_to_write)
        for endpoint in list_of_endpoints:
            endpoint_list_file.write(endpoint[1] + "\n")
    print("[] Done")


def get_all_endpoints(filepath: str) -> list:
    """
    Builds a list of tuples from the OAI-OMH Registered Data
    providers, filtered to those with .ac.uk addresses.
    Tuples in format (REPOSITORY NAME, BASE OAI URL, OAI-IDENTIFIER)
    :param filepath: STR filepath to the overall OAI-OMH spreadsheet
    :return: list of all registered URLs
    """
    print("[] Building list of endpoints from ", filepath)
    df = pd.read_excel(filepath, 'filtered')
    list_of_reg_data_providers = [tuple(x) for x in df.values]
    print("[] Done")
    return list_of_reg_data_providers

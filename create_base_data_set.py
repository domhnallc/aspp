from core_api_queries.core_query import get_core_providers_details, get_API_Key, base_query_api

def main():
    api_key = get_API_Key()
    print(api_key)
    institute_repo_details = get_core_providers_details('GB', api_key)
    print(institute_repo_details)

main()
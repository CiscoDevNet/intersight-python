import intersight
import re
import sys

def get_api_client(api_key_id, api_secret_file = None, private_key_string = None, proxy = None, endpoint="https://intersight.com"):
    if api_secret_file is None and private_key_string is None:
        print("Either api_secret_file or private_key_string is required to create api client")
        sys.exit(1)
    if api_secret_file is not None and private_key_string is not None:
        print("Please provide only one among api_secret_file or private_key_string")
        sys.exit(1)

    if api_secret_file is not None: 
        with open(api_secret_file, 'r') as f:
            api_key = f.read()
    else:
        api_key = private_key_string

    if re.search('BEGIN RSA PRIVATE KEY', api_key):
        # API Key v2 format
        signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15
        
    elif re.search('BEGIN EC PRIVATE KEY', api_key):
        # API Key v3 format
        signing_algorithm = intersight.signing.ALGORITHM_ECDSA_MODE_DETERMINISTIC_RFC6979
    
    configuration = intersight.Configuration(
        host=endpoint,
        signing_info=intersight.signing.HttpSigningConfiguration(
            key_id=api_key_id,
            private_key_string = api_key,
            signing_scheme=intersight.signing.SCHEME_HS2019,
            signing_algorithm=signing_algorithm,
            hash_algorithm=intersight.signing.HASH_SHA256,
            signed_headers=[
                intersight.signing.HEADER_REQUEST_TARGET,
                intersight.signing.HEADER_HOST,
                intersight.signing.HEADER_DATE,
                intersight.signing.HEADER_DIGEST,
            ]
        )
    )

    return intersight.ApiClient(configuration)
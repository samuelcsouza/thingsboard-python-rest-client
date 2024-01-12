import logging
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
# Importing the API exception
from tb_rest_client.rest import ApiException

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = "http://localhost:8080"
# Default Tenant Administrator credentials
username = "tenant@thingsboard.org"
password = "tenant"

def main():
    # Creating the REST client object with context manager to get auto token refresh
    with RestClientCE(base_url=url) as rest_client:
        try:
            rest_client.login(username=username, password=password)
            user = rest_client.get_user()
            devices = rest_client.get_customer_device_infos(customer_id=CustomerId(user.id.id, 'CUSTOMER'), page_size=10,
                                                            page=0)
            logging.info("Devices: \n%r", devices)
        except ApiException as e:
            logging.exception(e)


if __name__ == '__main__':
    main()
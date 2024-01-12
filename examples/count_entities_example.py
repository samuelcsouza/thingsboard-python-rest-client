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


# Creating the REST client object with context manager to get auto token refresh
with RestClientCE(base_url=url) as rest_client:
    try:
        rest_client.login(username=username, password=password)
        # Create entity filter to get all devices
        entity_filter = EntityFilter()

        # Create entity count query with provided filter
        devices_query = EntityCountQuery(entity_filter)

        # Execute entity count query and get total devices count
        devices_count = rest_client.count_entities_by_query(devices_query)
        logging.info("Total devices: \n%r", devices_count)
    except ApiException as e:
        logging.exception(e)
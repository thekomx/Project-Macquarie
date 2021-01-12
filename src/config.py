from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

secret_client = SecretClient(vault_url='https://projectmacquarie.vault.azure.net/', credential=DefaultAzureCredential())

api_key = secret_client.get_secret('financialmodelingprepAPI').value
db_connection_string = secret_client.get_secret('azSQLconnectionStr').value

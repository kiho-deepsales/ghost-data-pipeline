from google.oauth2 import service_account
import pandas_gbq

from config import PROJECT_ID, GOOGLE_APPLICATION_CREDENTIALS


def load_table(dataset_name, table_name):
    query = f"""
    SELECT *
    FROM `{PROJECT_ID}.{dataset_name}.{table_name}`
    """
    credentials = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS)
    print("Loading table...")
    table = pandas_gbq.read_gbq(query, project_id=PROJECT_ID, credentials=credentials)
    return table
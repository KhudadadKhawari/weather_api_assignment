from pymongo import MongoClient
USERNAME = 'db_created_username'  # ADD USERNAME
PASSWORD = 'db_created_password'  # Add PASSWORD
DATABASE = 'assignment'

CONNECTION_STRING = f"mongodb://{USERNAME}:{PASSWORD}@weather-shard-00-00.k9v1a.mongodb.net:27017,weather-shard-00-01.k9v1a.mongodb.net:27017,weather-shard-00-02.k9v1a.mongodb.net:27017/{DATABASE}?ssl=true&replicaSet=atlas-u126od-shard-0&authSource=admin&retryWrites=true&w=majority"


def get_database(database_name):
    client = MongoClient(CONNECTION_STRING)
    return client[f'{database_name}']



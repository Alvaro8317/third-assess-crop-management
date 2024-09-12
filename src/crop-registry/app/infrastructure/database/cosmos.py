import azure.cosmos.cosmos_client as cosmos_client
from app.config.cosmos import settings
import azure.cosmos.exceptions as exceptions


def _create_or_get_database(client):
    database_id = settings.get("database_id")
    try:
        db = client.create_database(id=database_id)
        print('Database with id \'{0}\' created'.format(database_id))
    except exceptions.CosmosResourceExistsError:
        db = client.get_database_client(database_id)
        print('Database with id \'{0}\' was found'.format(database_id))
    return db


class CosmosDBSingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CosmosDBSingleton(metaclass=CosmosDBSingletonMeta):
    def __init__(self):
        self.settings = settings
        self.client = self._initialize_client()
        self.database = _create_or_get_database(self.client)

    def _initialize_client(self):
        host = self.settings['host']
        master_key = self.settings['master_key']
        return cosmos_client.CosmosClient(host,
                                          {'masterKey': master_key},
                                          user_agent="CosmosDBPythonQuickstart",
                                          user_agent_overwrite=True)

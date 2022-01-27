from abc import ABC, abstractmethod
import redis

class NotFoundInDatabaseError(Exception):
    "Raised when data is not found in database"


class Database(ABC):

    @abstractmethod
    def connect(self):
        pass 

    @abstractmethod
    def get_data(self):
        pass


class RedisDatabase(Database):
    "A class implementing Database using Redis."
    
    def __init__(self, host='localhost', port=6379) -> None:
        self.host = host
        self.port = port
        self.redis_client = self.connect()

    def connect(self):
        print('Connecting to Redis server...')
        try:
            redis_client = redis.Redis(host=self.host, port=self.port)
            redis_client.ping()
            print('Connection successful.')
            return redis_client
        except Exception as e:
            print('Connection failed!!!')
            print(e)         

    def get_data(self, key):
        """ Returns data from database"""
        data = self.redis_client.get(key)
        if not data:    
            raise NotFoundInDatabaseError("Data was not found in database")

        return data



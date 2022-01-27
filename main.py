from cache import CacheMechanism, TimeBasedCache
from database import Database, NotFoundInDatabaseError, RedisDatabase


class CacheApplication():

    def __init__(self, database: Database, cache_mechanism: CacheMechanism) -> None:
        self.database = database
        self.cache = cache_mechanism

    def get(self, key):
        data = self.cache.get_data(key)
        if not data:
            try:
                data = self.database.get_data(key)
                self.cache.set_data(key, data)

            except NotFoundInDatabaseError as e:
                return e
        
        return data


if __name__ == '__main__':
    database = RedisDatabase()
    cache = TimeBasedCache(5)

    app = CacheApplication(database=database, cache_mechanism=cache)


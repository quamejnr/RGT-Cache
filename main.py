import time
from abc import ABC, abstractmethod


class CacheMechanism(ABC):
    """A class to implement caching mechanism"""
    
    cache = {}
    database = [1,2,3,4,5]

    @abstractmethod
    def get_data_from_database(self, data):
        pass

    @abstractmethod
    def get_data(self, data):
        pass
    
    @abstractmethod
    def set_data(self, data):
        pass


class TimeBasedCache(CacheMechanism):
    """A class to implement time-based cache mechanism"""

    def __init__(self, cache_time_limit) -> None:
        self.cache_time_limit = cache_time_limit

    def get_data_from_database(self, data):
        """ Returns data from database"""
        if data in self.database:
            return data

    def get_data(self, data):
        """ Returns data from cache if present and database if absent"""
        # check if data is in cache and elapsed time hasn't exceeded time limit.
        for last_cached_time, cached_data in self.cache.items():
            elapsed_time_since_last_cached = time.time() - last_cached_time
            if data == cached_data and elapsed_time_since_last_cached < self.cache_time_limit:
                return cached_data

        # fetch data from database if data is absent
        fetched_data = self.get_data_from_database(data)
        
        # set data
        return self.set_data(fetched_data)


    def set_data(self, data):
        """ Caches data with a timestamp."""
        cached_time = time.time()
        self.cache[cached_time] = data
        return data

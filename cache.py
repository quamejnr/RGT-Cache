from abc import ABC, abstractmethod
from cachetools import TTLCache
import time
from database import Database

    
class CacheMechanism(ABC):
    """A class to implement caching mechanism"""

    @abstractmethod
    def get_data(self, data):
        pass
    
    @abstractmethod
    def set_data(self, data):
        pass


class TimeBasedCache(CacheMechanism):
    """A class to implement time-based cache mechanism"""

    def __init__(self, cache_time_limit_in_seconds) -> None:
        self.cache_time_limit_in_seconds = cache_time_limit_in_seconds
        self.cache = TTLCache(maxsize=30, ttl=self.cache_time_limit_in_seconds)  # creates a dictionary which deletes data after a time limit


    def get_data(self, id):
        """ Returns data from cache """
        if id in self.cache:
            return self.cache[id]

    def set_data(self, id, data):
        """ Caches data"""
        self.cache[id] = data
        return data



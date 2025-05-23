from functools import lru_cache
from .config import CACHE_SIZE

def default_cache():
    return lru_cache(maxsize=CACHE_SIZE)
# API - Application Programming Interface
'''
Application - any software with a distinct function
Interface - contract of service between two applications
'''

# software intermediary that allows two applications to talk to each other
# receives data and gives data back

# functools - lru_cache()
'''
lru_cache() helps in reducing the execution time of the function using memoization technique

SYNTAX- @lru_Cache(maxsize = 128, typed = FALSE)
- maxsize - size of the cache, if maxsize is set to None, the cache can grow without limitations
- typed - if typed is set to True then function arguments of different types will be cached separately. For example f(3) and f(3.0) will be
          treated a distinct calls and they will be stored in two separate entries in the cache
'''

# TTLCache

'''
@cached(cache = TTLCache(maxsize=2, ttl=900))
Time to live Cache - it takes two parameters -  "maxsize" and "TTL"
TTL - states how long the cache should be stored. Value is in seconds
'''
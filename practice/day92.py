# memory caching
from functools import lru_cache
import time 

@lru_cache(maxsize=None)
def double(n):
    time.sleep(3)
    return n*2

print(f"Double of 5 after 3 sec is {double(5)}")
print(f"Double of 3 after 3 sec is {double(3)}")
print(f"Double of 6 after 3 sec is {double(6)}")
print()
print()
print(f"Double of 5 is {double(5)}")
print(f"Double of 3 is {double(3)}")
print(f"Double of 6 is {double(6)}")
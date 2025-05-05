import time

def cache(func):
    cache_value = {} 
    def wrapper(*args):
        start = time.time()
        if args in cache_value:
            end = time.time()
            print(f"{func.__name__} ran in {end-start} time")
            return cache_value[args]
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        cache_value[args] = result
        print(f"Cache values: {cache_value}")  
        return result
    return wrapper

@cache
def long_run(a, b):
    time.sleep(8)
    return a + b

print(long_run(2, 3))
print(long_run(2, 3))
print(long_run(4, 3))
print(long_run(4, 7))
print(long_run(4, 3))
print(long_run(2, 3))

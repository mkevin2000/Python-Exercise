import functools
import time
def performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return elapsed_time, result
    return wrapper 
@performance
def add(a, b):
    return a + b

time_taken, sum_result = add(1, 2)
print(sum_result)   # 3
print(time_taken)   # 0.000001...
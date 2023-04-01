import functools
import logging
import time
import sys


def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        logging.info(f"Returned {result} from {func.__name__} in {elapsed_time:.6f} seconds")
        return result
    return wrapper


# Decorate the built-in len function
len = log_function_call(len)

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])

print(len("Naomi"))

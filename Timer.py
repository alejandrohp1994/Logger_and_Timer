import Logger
from time import time


def timer(function):
    def wrapper(*args, **kwargs):
        
        start = time()
        
        function(*args, **kwargs)
        
        end = time()
        elapsed_time = round( float( end - start), 2)

        Logger.log(function.__name__, elapsed_time, "SUCCESS")

    return wrapper

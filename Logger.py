import datetime
import os

def is_in_folder(PATH):
    if os.path.exists(PATH) == False:
        pass

def log(function_name, elapsed_time, status):
    
    PATH = os.getcwd() + r'/Logs/timer.txt'
    
    current_time = str(datetime.datetime.now()).split(".")[0]

    with open(PATH, "a+") as file:
        file.write( f"[{current_time}] [{status}] Function: '{function_name}' took {elapsed_time} seconds." )
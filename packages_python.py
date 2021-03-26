from random import random # generates random numbers
import math

print(random())
num_float = 23.6

print("Actual float value " + str(num_float))
print(math.ceil(num_float)) # if number .5 round it up
print(num_float.__round__())

print(math.floor(num_float)) # if number .4 or less round it down

# Python Modules
import os
import datetime, sys

working_directory = os.getcwd() # it tells us the current dir location
print(working_directory)

# Some commands doesn't work for Windows
# print(os.uname())

print(os.cpu_count())
print(datetime.date.today())
print(sys.path)
print(math.pi)

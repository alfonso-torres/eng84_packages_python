# Python packages
Packages are namespaces which contain multiple packages and modules themselves. A Python package
is a collection of modules, a simple directory of Python modules that contains different
scripts. They are a simply directories but with a twist. <br/>
Each package in Python is a directory which must contain a special file called `__init__.py`. 
This file can be empty, and it indicates that the directory it contains is a Python package, 
so it can be imported the same way a module can be imported.

### Why should we use them
Python provides advantages of using packages:
1. Naming conflicts can be solved easily.
2. Improves the Modularity of the application.
3. It allows to organize the code into smaller pieces that will be easier to manage.
4. The code in the modules can be reloaded and run as many times as needed.
### Python Modules
Modules in Python are separate code groupings which packages program code and data
for re-use. Modules that are related to each other are mainly put in the same package.
When a module from an external package is required in a program, that package can be 
imported and its modules can be put to use. So a package saves modules, and these modules 
contains executables statements as well as function definitions that we will be able to use in any program.
Let's see an example:
````python
import math # Package math

# Let's use some modules from math
num_float = 23.6
print("Actual float value " + str(num_float))
print(math.ceil(num_float)) # if number .5 round it up
print(math.floor(num_float)) # if number .4 or less round it down
print(math.pi)
````
````python
import os
import datetime, sys

working_directory = os.getcwd() # it tells us the current dir location
print(working_directory)
print(os.cpu_count())
print(datetime.date.today())
print(sys.path)
````
### What is pip
Pip is a package management system used to install and manage software packages 
written in Python. As we know a package contains all the files you need for 
a module. So these modules are Python code libraries that you can include in your 
project.
- `pip` is package manager in Python to install packages.
- To check if pip is installed, type the following command:
````commandline
pip --version
````
- To install PIP in the case do not have pip installed, you can download and 
  install it from this [link](https://pypi.org/project/pip/).
- To use pip:
````commandline
pip install package_name
````
- To list all the packages installed on your system:
````commandline
pip list
````

## Let's see an example:
Create a function called status_code_check to check the status of a website. <br/>
- To install the package request:
````commandline
pip3 install requests
````
Function should return status code with appropriate message. <br/>
DRY.
````python
import requests
website = input("Please enter the website you would like to check his status (INCLUDE the http//): ")

def status_code_check(name):
    response = requests.get(name)
    
    if response:
        print(f"Success with status code {response.status_code}.")
    else:
        print("Something went wrong with status code {response.status_code}.")

status_code_check(website)
# We can see the benefits of using packages in the conditions statements
# They will return any code without asking conditions in the "if" statement 
````

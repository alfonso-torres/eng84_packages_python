# Python request package
# Let's connect to live web using python requests api
# We will connect to www.bbc.com and check if the web is live

import requests

# def check_status():
#    response = requests.get("http://www.bbc.co.uk/")
#    if response:  # the condition was True
#        print("Success and the status code " + str(response.status_code))
#    elif response:
#        print("Failure.")
#    elif response:
#        print("OOPs something went wrong.")
# print(check_status())

response = requests.get("https://www.bbc.co.uk")
# Response object overwrites __bool__ method (class polymorphism) to check status code
# Returns True if self.status_check < 400
if response:
    print(f"Success with status code {response.status_code}")
else:
    print("Something went wrong.")

# requests goes one step further in simplifying this process for us
# if you use response instance in a condition expression
# it will evaluate to True if the status code was between 200 and 400, False otherwise
# therefore, you can can simplify the last example by rewriting the if statement as above
# In this way it simplifies our code

# responses = requests.get("http://www.bbc.co.uk/")
# if responses.status_code == 200:
#    print("This website is up and running, status code is: " + str(responses.status_code))
# else:
#    print("OOPs something went wrong, status code is: " + str(responses.status_code))
# status 200 which a success means the website is live running
# status 400 or 404 means not working

# create a function called status code check
# function should return status code with appropriate message

# create a function called status code check
# function should return status code with appropriate message
# DRY

# website = input("Please enter the website you would like to check his status (INCLUDE the http//): ")

# def status_code_check(name):
#    responses = requests.get(name)

#    if responses.status_code == 200:
#        return ("This website is up and running, status code is: " + str(responses.status_code))
#    else:
#        return ("OOPs something went wrong, status code is: " + str(responses.status_code))

#print(status_code_check(website))


website = input("Please enter the website you would like to check his status (INCLUDE the http//): ")

def status_code_check(name):
    response = requests.get(name)

    if response:
        print(f"Success with status code {response.status_code}.")
    else:
        print(f"Something went wrong with status code {response.status_code}.")

status_code_check(website)

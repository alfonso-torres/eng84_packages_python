# API for postcode.io

import requests

url = "http://api.postcodes.io/postcodes/" #API where we will get the result
postcode = "e147le"

url_arg = url + postcode
print(url_arg)

# method sends a GET request to the specified url - Make a request to a web page
response = requests.get(url_arg)
print(response.status_code) # return the status code
response_dict = response.json() # Get the results in format JSON
response_keys = response_dict["result"]
# Let's get some information from the postcode we requested
for items in response_keys.keys():
    if items == "postcode":
        print("Your postcode locations is " + str(response_keys["postcode"]))

    if items == "longitude":
        print("Your longitude is " + str(response_keys["longitude"]))
    elif items == "latitude":
        print("Your latitude is " + str(response_keys["latitude"]))

# print(response.__dict__)
#print(type(response_dict))

#result_dict = response_dict["result"]
#for key, val in result_dict.items():
#    print(key, val)

#for key in response_dict.keys():
#    print(key)
#    if key == "result":
#        print(response_dict[key]['postcode'])

#print(response.content)
#print(response.headers)
#print(response.history)
#print(response.cookies)
#print(response.encoding.isdigit())
#print(response.headers.keys())
#print(response.is_redirect)

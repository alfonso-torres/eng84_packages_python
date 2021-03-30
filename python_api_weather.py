import requests

class API_Weather():
    def __init__(self):
        self.postcode_url = "https://api.postcodes.io/postcodes/"
        self._greetings()

    # Say welcome to the customer
    def _greetings(self):
        print("WELCOME! Let's go to check the weather in your zone :) ")

    # Function to get the weather from a postcode
    def get_weather(self, postcode):
        url_arg = self.postcode_url + postcode
        response = requests.get(url_arg)

        if response:
            response_dict = response.json()  # Get the results in format JSON
            response_keys = response_dict["result"]
            # Let's get the city information from the postcode we got
            for items in response_keys.keys():
                if items == "region": # Get the city from the postcode
                    weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + str(response_keys["region"]) + "&APPID=5e9534b4a243e7da54036aab66615bf1"
                    response_weather = requests.get(weather_url) # Get the weather with the city we got it
                    response_dictionary = response_weather.json()
                    weather_result = response_dictionary["weather"]
                    region = str(response_keys["region"])
                    print("Postcode validated! Proceeding to get the weather...")
                    # Let's print the result, the weather
                    print(f"The weather in the area related to your postcode ({postcode} - {region}) is : {weather_result}" )
                    return True
        else:
            return False

get_result = API_Weather()

run_program = True
while run_program:
    user_input = input("Please enter the postcode you would like to get the weather: ")
    if not user_input:
        print("Your postcode is empty...")
    else:
        if get_result.get_weather(user_input) == False:
            print("Please check you introduce a valid postcode...")
        else:
            run_program = False


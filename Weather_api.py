#It's my little work 
# i used weather api's api to get weather info
#if you wanna use this you can sing in and get your own api 

import  requests
from pprint import pprint # for printing the json into tree formate !

def weather_info(city):
    API_KEY='#your API key '
    basic_url="https://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city
    data = requests.get(basic_url).json()
    weather = data['weather']
    weather_data = weather[0]
    weather_info = weather_data['description']
    wind_info = data['wind']
    temp_data=data['main']
    temp=temp_data['temp']
    temp_max=temp_data['temp_max']
    temp_min=temp_data['temp_min']
    return weather_info,wind_info,temp,temp_min,temp_max

def temp_convert(temp,min_temp,max_temp):
    temperature=[temp,min_temp,max_temp]
    converted_celsius=[]
    converted_faranheit=[]
    for temp_celsius in temperature:
        celsius=temp_celsius-273.15
        converted_celsius.append(celsius)
    for temp_faranheit in temperature:
        yo=temp_faranheit-273.17
        faranheit=9/5*yo +32
        converted_faranheit.append(faranheit)
    return converted_faranheit,converted_celsius



def main(c):
    city=c
    weather,wind,temp,temp_min,temp_max=weather_info(city)
    faranheit,celsius=temp_convert(temp,temp_min,temp_max)
    print(f"City: {city}")
    print(f"Weather: {weather}")
    print(f"Farenheit-->Temp,Min_temp,Max,temp: {faranheit}")
    print(f"Celsius-->Temp,Min_temp,Max,temp: {celsius}")
    print(f"Wind: {wind}")

if __name__=="__main__":
    while True:
        city=input("City: ")
        if city in ["exit","quit","bye","stop"]:
            exit()
        main(city)

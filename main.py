#tkinter is used as a graphical user interface tool.
from tkinter import *
from tkinter import messagebox
import requests
import datetime
#Search button outputs are defined here.
def search():
    city = city_entry.get()
    weather = get_weather(city)
#Labels are filled with the values returned from the URL.
    if weather:
        location_label["text"] = "{}, {}".format(weather[0], weather[1])
        img["file"] = 'weather_icons/{}.png'.format(weather[8])
        temp_label["text"] = "Temperature:{:.1f}°F, Feels Like : {:.1f}°F, Humidity : {} % , Wind Speed {} ".format(weather[2], weather[3], weather[4],weather[5])
        weather_info["text"] = "{}, {}".format(weather[6], weather[7])
        time_label["text"] = "{}".format(get_date(weather[9]))
#If an incorrect value is entered, the error message will be displayed here.
    else:
        messagebox.showerror("Error", "Location Not Found !")
#Since there is a separate time zone for each location,
#Timezones are pulled here from the web-site.
def get_date(timezone):
    tz = datetime.timezone(datetime.timedelta(seconds=int(timezone)))
    return datetime.datetime.now(tz = tz).strftime("%m/%d/%Y, %H:%M:%S")
#Url and PyCharm connection is made here.
def get_weather(city) :
    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=a34e3ec31b819c7f38d61701645d72e6&q=" #bu link openweathermapten alinir, key dahil
    url = api_address + city
    response = requests.get(url)
#Here are the specific values I pulled from the site.
    if response :
        result = response.json()
        city = result["name"]
        country = result["sys"]["country"]
        temp_kelvin = result["main"]["temp"]
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        temp_feels_lk = result["main"]["feels_like"]
        temp_feels_lk_fahrenheit = (temp_feels_lk - 273.15) * 9 / 5 + 32 #kelvin to fahrenheit formula
        temp_humidity = result["main"]["humidity"]
        wind_speed = result["wind"]["speed"]
        weather_type = result["weather"][0]["main"]
        weather_description = result["weather"][0]["description"]
        icon = result["weather"][0]["icon"]
        timezone = result["timezone"]
        final = (city, country, temp_fahrenheit, temp_feels_lk_fahrenheit, temp_humidity, wind_speed, weather_type,
                 weather_description, icon, timezone)
        return final
    else:
        return None
#Interface design is done here.
weatherapp= Tk()
weatherapp.title("Leidos Weather Application")
weatherapp.geometry("700x350")
#Each code after this is used for a label and button design.
city_entry = Entry(weatherapp, textvariable=StringVar() , font ="{Comic Sans MS}")
city_entry.pack()

search_btn = Button(weatherapp, text="Get Weather Info", width=15, command=search , font ="{Comic Sans MS}")
search_btn.pack()

location_label = Label(weatherapp, text="", font=("{Comic Sans MS}",  20))
location_label.pack()

img = PhotoImage(file="")
image = Label(weatherapp, image=img, bg= "#add8e6")
image.pack()

weather_info = Label(weatherapp, text="", font="{Comic Sans MS}")
weather_info.pack()

temp_label = Label(weatherapp , text="", font ="{Comic Sans MS}")
temp_label.pack()

time_label = Label(weatherapp, text="", font="{Comic Sans MS}" )
time_label.pack()

weatherapp.mainloop()
#-*- coding: utf-8 -*-
from geopy.geocoders import Nominatim
loc = Nominatim(user_agent="None")
# print lat,lon of each country from our data
def pos_print(country):
    try:
        loc = Nominatim(user_agent="None")
        pos=loc.geocode("{}".format(country))
        positon = [pos.latitude , pos.longitude]
        return positon
    except AttributeError as err:
        print("Something went wrong when looking up that country!")
        print(err)


a = pos_print("Republic of Georgia")
print(a)
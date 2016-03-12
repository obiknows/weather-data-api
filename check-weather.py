#
# check-weather.py
#
# by - sam nnodim (son2105)
#
# adapted from: https://github.com/mikedewar/RealTimeStorytelling

# import some very useful libs
from sys import stdout
import numpy as np
import requests
import json
import time

#
url = "https://api.forecast.io/forecast/"
apikey = "4ec099acc7de343d9c3db9d286aca570" # DarkSkyForecast API key
coords = "/40.806290,-73.963005" # lat, long coordinates

# Set poission param. (2 minutes)
rate = 10

while True:
    # send a GET request to the OWM API and turn it to JSON data
    data = requests.get( url + apikey + coords ).json()

    # get the distance of the nearest storm from the data
    storm = data["currently"]["nearestStormDistance"]

    # Print current weather pressure from params
    print ( json.dumps({"stormDistance": storm}) )
    stdout.flush()

    # set the sleep rate as a randomn exponential value
    # draw time beteween events from a random distribution
    time.sleep( np.random.exponential(rate) )

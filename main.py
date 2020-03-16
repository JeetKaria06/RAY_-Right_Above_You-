import requests
import argparse
import json
from datetime import datetime

# parsing arguments for variable input by user at runtime
ap = argparse.ArgumentParser()
ap.add_argument("-lat", "--latitude", required=True, help="Latitude of the location")
ap.add_argument("-lon", "--longitude", required=True, help="Longitude of the location")
args = vars(ap.parse_args())

#method to see the content of json object in sorted manner of the key
def jPrint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# creating parameters
parameters = {
    "lat":args["latitude"],
    "lon":args["longitude"]
}

# making request to the API-URL with specified parameters
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)


pass_times = response.json()['response']

t = []
times = []

for time in pass_times:
    tmp = time['risetime']
    t.append(tmp)

for rt in t:
    tmp = datetime.fromtimestamp(rt)
    times.append(tmp)
    print(tmp)

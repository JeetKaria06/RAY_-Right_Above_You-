import requests
import json
import sys
from datetime import datetime

def jPrint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

parameters = {
    "lat":(sys.argv[1]),
    "lon":(sys.argv[2])
}

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
























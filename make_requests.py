import json
import requests

increment = 1000
url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/"
headers = {"token": "JnskqlFozmUWRgZZLRtNQGDwJKPaneqm"}
params = {"limit": increment, "offset": 0}

count = 0
while True:
    response = requests.get(url, headers=headers, params=params)
    print(count, response.status_code)
    r_json = response.json()

    name = "locations_" + str(count) + ".json"
    with open(name, 'w') as f:
        json.dump(r_json, f)

    params["offset"] += increment
    count += 1

    if params["offset"] > r_json['metadata']['resultset']['count']:
        break

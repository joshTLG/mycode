import urllib.request
import requests
import json
import time

def main():
    
    # load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
  
    # Extract the ISS location
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']
  
    # Ouput to the terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # My latitude and longitude


if __name__ == "__main__":
    main()

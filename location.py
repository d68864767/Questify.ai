```python
# location.py

import requests
import config

class Location:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_location(self):
        # Use a location service API to get the current location
        # For example, we can use the IP Geolocation API
        response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={self.api_key}')

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Extract the latitude and longitude
            latitude = data['latitude']
            longitude = data['longitude']

            return latitude, longitude
        else:
            return None

    def get_location_details(self, latitude, longitude):
        # Use a location service API to get details about a location
        # For example, we can use the Google Places API
        response = requests.get(f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&key={self.api_key}')

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Extract the details about the location
            details = data['results']

            return details
        else:
            return None
```

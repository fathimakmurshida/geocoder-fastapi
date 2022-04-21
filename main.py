from fastapi import FastAPI

import geocoder

app = FastAPI()
async def root():
    return {"message": "Hello World"}



@app.get('/location')
def forward(address:str):
    try:
        geolocator = geocoder.osm(address)
        address = geolocator.json['raw']['display_name']
        lat = geolocator.json['raw']['lat']
        lon = geolocator.json['raw']['lon']
        data = {
            "source": "OSM",
            "longitude": lat,
            "latitude": lon, 
            "address": address
        }
        return data
    except Exception:
        return {"Internal Server Error."} 
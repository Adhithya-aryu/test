# importing modules
from geopy.geocoders import Nominatim

# calling the nominatim tool
geoLoc = Nominatim(user_agent="summa")

# passing the coordinates
lat = 40.56487333333333
log = -73.91181166666667
locname = geoLoc.reverse(f"{lat},{log}")

# printing the address/location name
print(locname.address)
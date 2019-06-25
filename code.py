##Este es un markdown to test the capstone project ##
import requests # library to handle requests
import pandas as pd # library for data analsysis
import numpy as np # library to handle data in a vectorized manner
import random # library for random number generation

!conda install -c conda-forge geopy --yes 
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values

# libraries for displaying images
from IPython.display import Image 
from IPython.core.display import HTML 
    
# tranforming json file into a pandas dataframe library
from pandas.io.json import json_normalize

!conda install -c conda-forge folium=0.5.0 --yes
import folium # plotting library

print('Folium installed')
print('Libraries imported.')

CLIENT_ID = 'YHPGVQ3YPTNFEUP1VRC4IAWP0AJ0KXCP5JIFDXWUCHQDRRG5' # your Foursquare ID
CLIENT_SECRET = 'ZYWNKKTKYHIBFYM2VDYVTZQTWUNBF5Y1BP2RPAI45FW53ET5' # your Foursquare Secret
VERSION = '20190623'
LIMIT = 30
print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)
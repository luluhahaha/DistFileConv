import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

feeder_7773 = pd.read_csv("./Bus_coordinates_7773.csv")
se_re = pd.read_csv("./Node_connections_7773.csv")

se_lon = []
se_lat = []
re_lon = []
re_lat = []
se_busID = []
re_busID = []

temp = list(feeder_7773["Bus_ID"])
bus_ID_cap = []
for s in temp:
    caps = s.upper()
    bus_ID_cap.append(caps)

temp = list(se_re["From_node"])
se_cap = []
for s in temp:
    caps = s.upper()
    se_cap.append(caps)


temp = list(se_re["To_node"])
re_cap = []
for r in temp:
    caps = r.upper()
    re_cap.append(caps)


for s in se_cap:
    temp2 = bus_ID_cap.index(s)
    if temp2 >=0:
        lon = feeder_7773["Longitude"][temp2]
        lat = feeder_7773["Latitude"][temp2]
        se_busID.append(s)
        se_lon.append(lon)
        se_lat.append(lat)

for r in re_cap:
    temp2 = bus_ID_cap.index(r)
    if temp2 >=0:
        lon = feeder_7773["Longitude"][temp2]
        lat = feeder_7773["Latitude"][temp2]
        re_busID.append(r)
        re_lon.append(lon)
        re_lat.append(lat)


## Writing to an CSV file using Python
import csv

with open('se_re_lon_lat.csv', mode='w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(['se_lon', 'se_lat', 're_lon', 're_lat', 'se_busID', 're_busID'])
    for i in range(0, len(se_lon)):
        writer.writerow([se_lon[i], se_lat[i], re_lon[i], re_lat[i], se_busID[i], re_busID[i]])

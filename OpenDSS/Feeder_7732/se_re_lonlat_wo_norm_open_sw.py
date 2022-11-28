import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

feeder_7732 = pd.read_csv("./Bus_coordinates_7732.csv")
se_re = pd.read_csv("./Node_connections_7732_wo_norm_open_sw.csv")



temp = list(feeder_7732["Bus_ID"])
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

new_list=se_cap+re_cap

unique_elements = [] # empty list to hold unique elements from the list
dup_elements = [] # empty list to hold the duplicate elements from the list
for i in new_list:
    if i not in unique_elements:
        unique_elements.append(i)
    else:
        dup_elements.append(i)


busID_cap2 = []
bus_lon = []
bus_lat = []
for u in unique_elements:
    temp2 = bus_ID_cap.index(u)
    if temp2 >=0:
        lon = feeder_7732["Longitude"][temp2]
        lat = feeder_7732["Latitude"][temp2]
        busID_cap2.append(u)
        bus_lon.append(lon)
        bus_lat.append(lat)


## Writing to an CSV file using Python
import csv

with open('Bus_coordinates_7732_no_sw.csv', mode='w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(['Bus_ID', 'Longitude', 'Latitude'])
    for i in range(0, len(busID_cap2)):
        writer.writerow([busID_cap2[i], bus_lon[i], bus_lat[i]])







se_lon = []
se_lat = []
re_lon = []
re_lat = []
se_busID = []
re_busID = []


for s in se_cap:
    temp2 = busID_cap2.index(s)
    if temp2 >=0:
        lon = bus_lon[temp2]
        lat = bus_lat[temp2]
        se_busID.append(s)
        se_lon.append(lon)
        se_lat.append(lat)

for r in re_cap:
    temp2 = busID_cap2.index(r)
    if temp2 >=0:
        lon = bus_lon[temp2]
        lat = bus_lat[temp2]
        re_busID.append(r)
        re_lon.append(lon)
        re_lat.append(lat)


## Writing to an CSV file using Python
import csv

with open('se_re_lon_lat_nosw.csv', mode='w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(['se_lon', 'se_lat', 're_lon', 're_lat', 'se_busID', 're_busID'])
    for i in range(0, len(se_lon)):
        writer.writerow([se_lon[i], se_lat[i], re_lon[i], re_lat[i], se_busID[i], re_busID[i]])

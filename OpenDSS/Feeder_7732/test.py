# The purpose of this script is to
# identify nodes without coordinates

with open('Lines.dss') as f:
    lines = f.readlines()

with open('Loads.dss') as f:
    loads = f.readlines()

with open('Transformers.dss') as f:
    trafo = f.readlines()

with open('Capacitors.dss') as f:
    caps = f.readlines()

with open('Buscoords.dss') as f:
    buscoord = f.readlines()

# Line buses
line_se = []
line_re = []
fuse_list = []
three_phs_lines = []
two_phs_lines = []
one_phs_lines = []
three_phs_fuses = []
two_phs_fuses = []
one_phs_fuses = []
temp_col = []
for i in range(0, len(lines), 2):
    stri = lines[i]

    if stri[4:8] == 'Line':
        idx1 = stri.index('bus1')  # index of bus 1
        idx2 = stri.index('bus2')  # index of bus 2
        idx3 = stri.index('switch')  # index of switch
        bus1_name = stri[idx1 + 5:idx2 - 1]
        bus2_name = stri[idx2 + 5:idx3 - 1]
        line_se.append(bus1_name)
        line_re.append(bus2_name)

        temp = stri.index('phases')
        if stri[temp:temp+8] == 'phases=3':
            three_phs_lines.append(stri)
        elif stri[temp:temp+8] == 'phases=2':
            two_phs_lines.append(stri)
        elif stri[temp:temp+8] == 'phases=1':
            one_phs_lines.append(stri)
        else:
            print('Go figure')



    if stri[4:8] == 'Fuse':
        fuse = lines[i]
        fuse_list.append(fuse)
        temp = stri.index('monitoredobj')
        temp2 = stri.index(' ', temp+1)
        temp3 = stri[temp+13:temp2]
        temp_col.append(temp3)

# a=0
#
# for temp3 in temp_col:
#     for i in range(0, 20, 2):
#         stri = lines[i]
#     # while a <= len(temp_col)-1:
#     #     temp3 = temp_col[a]
#         tem = stri.find(temp3)
#             if tem >= 0:
#                 temp = stri.index('phases')
#                 if stri[temp:temp + 8] == 'phases=3':
#                     three_phs_fuses.append(stri)
#                 elif stri[temp:temp + 8] == 'phases=2':
#                     two_phs_fuses.append(stri)
#                 elif stri[temp:temp + 8] == 'phases=1':
#                     one_phs_fuses.append(stri)
#                 else:
#                     print('Go figure')
#     # a=a+1
#
#         for temp3 in temp_col:
#
#             if stri2[idx6+1:idx5-1] == temp3:
#
#                 temp = stri2.index('phases')
#                 if stri2[temp:temp + 8] == 'phases=3':
#                     three_phs_fuses.append(stri2)
#                 elif stri2[temp:temp + 8] == 'phases=2':
#                     two_phs_fuses.append(stri2)
#                 elif stri2[temp:temp + 8] == 'phases=1':
#                     one_phs_fuses.append(stri2)
#                 else:
#                     print('Go figure')





# Tranformer buses
trafo_se = []
trafo_re = []
three_phs_trafos = []
two_phs_trafos = []
one_phs_trafos = []
for i in range(0, len(trafo), 2):
    stri = trafo[i]
    idx1 = stri.index('bus')  # index of bus 1
    idx2 = stri.index('bus', idx1 + 1)  # index of bus 2
    idx3 = stri.index('wdg=2')  # index of winding
    idx4 = stri.index('XHL')  # index of winding
    bus1_name = stri[idx1 + 4:idx3 - 1]
    bus2_name = stri[idx2 + 4:idx4 - 1]
    trafo_se.append(bus1_name)
    trafo_re.append(bus2_name)

    temp = stri.index('phases')
    if stri[temp:temp + 8] == 'phases=3':
        three_phs_trafos.append(stri)
    elif stri[temp:temp + 8] == 'phases=2':
        two_phs_trafos.append(stri)
    elif stri[temp:temp + 8] == 'phases=1':
        one_phs_trafos.append(stri)
    else:
        print('Go figure')

trafos_num = [len(one_phs_trafos), len(two_phs_trafos), len(three_phs_trafos)]
lines_num = [len(one_phs_lines), len(two_phs_lines), len(three_phs_lines)]


# Load buses
load_bus_list = []
one_phs_loads = []
two_phs_loads = []
three_phs_loads = []
four_phs_loads = []
five_phs_loads = []
six_phs_loads = []
for i in range(0, len(loads), 2):
    stri = loads[i]
    idx1 = stri.index('bus1')  # index of bus 1
    idx2 = stri.index('kV')
    load_bus = stri[idx1 + 5:idx2 - 1]
    load_bus_list.append(load_bus)

    temp = stri.index('Phases')
    if stri[temp:temp + 8] == 'Phases=3':
        three_phs_loads.append(stri)
    elif stri[temp:temp + 8] == 'Phases=2':
        two_phs_loads.append(stri)
    elif stri[temp:temp + 8] == 'Phases=1':
        one_phs_loads.append(stri)
    elif stri[temp:temp + 8] == 'Phases=6':
        six_phs_loads.append(stri)
    elif stri[temp:temp + 8] == 'Phases=5':
        five_phs_loads.append(stri)
    elif stri[temp:temp + 8] == 'Phases=4':
        four_phs_loads.append(stri)
    else:
        print('Go figure')
    loads_num = [len(one_phs_loads), len(two_phs_loads), len(three_phs_loads), len(four_phs_loads), len(five_phs_loads), len(six_phs_loads)]

# Finding total value and active and reactive loads
Pload_list = []
Qload_list = []
for i in range(0, len(loads), 2):
    stri = loads[i]
    idx1 = stri.index('kW')  # index of bus 1
    idx2 = stri.index('kvar')
    idx3 = stri.index('Phases')
    kW = stri[idx1 + 3:idx2 - 1]
    kvar = stri[idx2 + 5:idx3 - 1]
    Pload_list.append(kW)
    Qload_list.append(kvar)

Pload_float = []
for i in Pload_list:
    temp_P = float(i)
    Pload_float.append(temp_P)
Total_Pload = sum(Pload_float)/1000 #in MW

Qload_float = []
for i in Qload_list:
    temp_Q = float(i)
    Qload_float.append(temp_Q)
Total_Qload = sum(Qload_float)/1000 #in MVAr

# Cap buses
cap_bus_list = []
for i in range(0, len(caps), 2):
    stri = caps[i]
    idx1 = stri.index('Bus1')  # index of bus 1
    idx2 = stri.index('phases')
    cap_bus = stri[idx1 + 5:idx2 - 1]
    cap_bus_list.append(cap_bus)

bus_list = line_se + line_re + trafo_se + trafo_re + load_bus_list + cap_bus_list

# Bus coordinates
bus_coord_list = []
for i in range(0, len(buscoord), 1):
    stri = buscoord[i]
    idx1 = stri.index(' ')  # index of bus 1
    bus_coord = stri[0:idx1]
    bus_coord_list.append(bus_coord)

# strings = ['This string has apples', 'This string has oranges', 'This string has neither']
# new_string = []
# for s in strings:
#     apples_index = s.find('apples')
#     if apples_index < 0:
#         print('Apples not in string')
#         new_string.append(s)
#     else:
#         print(f'Apples in string starting at index {apples_index}')
#         res_str = s.replace('apples', '')
#         new_string.append(res_str)

# new=[]
# for s in strings:
#     caps = s.upper()
#     print(f'upper case is written as {caps}')


# Eliminating phasing (.1.2.3) from bus list to make it comparable to bus coordinates files
new_bus_list = []

for s in bus_list:
    length = len(s)

    if s[length - 12:] == '.1.2.3.1.2.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 11] + replacement
        new_bus_list.append(res_str)

    elif s[length - 12:] == '.1.2.3.3.1.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 11] + replacement
        new_bus_list.append(res_str)

    elif s[length - 12:] == '.1.2.3.2.1.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 11] + replacement
        new_bus_list.append(res_str)

    elif s[length - 12:] == '.3.1.2.1.2.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 11] + replacement
        new_bus_list.append(res_str)

    elif s[length - 12:] == '.2.1.3.1.2.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 11] + replacement
        new_bus_list.append(res_str)

    elif s[length - 6:] == '.1.2.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        new_bus_list.append(res_str)

    elif s[length - 6:] == '.1.3.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        new_bus_list.append(res_str)

    elif s[length - 6:] == '.3.2.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        new_bus_list.append(res_str)

    elif s[length - 6:] == '.3.1.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        new_bus_list.append(res_str)


    elif s[length - 6:] == '.2.3.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        new_bus_list.append(res_str)

    elif s[length - 6:] == '.2.1.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        new_bus_list.append(res_str)

    elif s[length - 4:] == '.1.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        new_bus_list.append(res_str)

    elif s[length - 4:] == '.1.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        new_bus_list.append(res_str)

    elif s[length - 4:] == '.1.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        new_bus_list.append(res_str)

    elif s[length - 4:] == '.2.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        new_bus_list.append(res_str)

    elif s[length - 4:] == '.2.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        new_bus_list.append(res_str)

    elif s[length - 4:] == '.2.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        new_bus_list.append(res_str)

    elif s[length - 4:] == '.3.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        new_bus_list.append(res_str)

    elif s[length - 4:] == '.3.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        new_bus_list.append(res_str)

    elif s[length - 4:] == '.3.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        new_bus_list.append(res_str)

    elif s[length - 2:] == '.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 1] + replacement
        new_bus_list.append(res_str)

    elif s[length - 2:] == '.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 1] + replacement
        new_bus_list.append(res_str)

    elif s[length - 2:] == '.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 1] + replacement
        new_bus_list.append(res_str)

    else:
        new_bus_list.append(s)

# # First convert buscoords list to uppercase
upper_bus_coords = []
for s in bus_coord_list:
    caps = s.upper()
    # print(f'upper case is written as {caps}')
    upper_bus_coords.append(caps)

# convert bus list to uppercase
upper_bus_list = []
for s in new_bus_list:
    caps = s.upper()
    # print(f'upper case is written as {caps}')
    upper_bus_list.append(caps)

real_bus_set = set(upper_bus_list)  # unique bus list in uppercase
real_bus_list = list(real_bus_set)

# Checking which buses do not have coordinates
res = [x for x in real_bus_list + upper_bus_coords if x not in upper_bus_coords]

# Checking redundant buses which have buscoords
redundant = [x for x in real_bus_list + upper_bus_coords if x not in real_bus_list]

# s = '30907300001-XFO.2'
# pt2 = s.find('.2')
# temp = s[pt2 + 1:]
# temp
# res_str = temp.replace('.2', '')
# res_str=s[:pt2 + 1]+res_str
# res_str



## Plotting on a map
import pyproj

wgs84 = pyproj.Proj(projparams = 'epsg:4326')
InputGrid = pyproj.Proj(projparams = 'epsg:3857')

real_bus_coords = []
for r in range(0, len(real_bus_list)):
    if real_bus_list[r] in upper_bus_coords:
        temp = upper_bus_coords.index(real_bus_list[r])
        real_bus_coords.append(buscoord[temp])
        # print('Found')


# x_pixel_range = 1200
# y_pixel_range = 800
# x_list = []
# y_list = []
# for i in range(0, len(real_bus_coords), 1):
#     stri = real_bus_coords[i]
#     idx1 = stri.index(' ')
#     idx2 = stri.index(' ', idx1 + 1)
#     x_temp = float(stri[idx1+1:idx2])
#     y_temp = float(stri[idx2 + 1:len(stri)-1])
#     x_list.append(x_temp)
#     y_list.append(y_temp)
#
# try:
#     x_scale = x_pixel_range / (max(x_list) - min(x_list))
#     x_b = -x_scale * min(x_list)
#     y_scale = y_pixel_range / (max(y_list) - min(y_list))
#     y_b = -y_scale * min(y_list)
# except:
#     x_scale, x_b, y_scale, y_b = (0, 0, 0, 0)
#
# lat_list = []
# lon_list = []
# buscoord_lon_lat = []
# for i in range(0, len(real_bus_coords), 1):
#     stri = real_bus_coords[i]
#     idx1 = stri.index(' ')
#     lat = str(x_scale * float(x_list[i]) + x_b)
#     lon = str(800 - (y_scale * float(y_list[i]) + y_b))
#     buscoord_lon_lat.append([stri[0:idx1], lat, lon])
#     lat_list.append(lat)
#     lon_list.append(lon)







bus_list = []
x_list = []
y_list = []
lat_list = []
lon_list = []
buscoord_lon_lat = []
for i in range(0, len(real_bus_coords), 1):
    stri = real_bus_coords[i]
    idx1 = stri.index(' ')
    idx2 = stri.index(' ', idx1 + 1)
    x_temp = float(stri[idx1+1:idx2])
    y_temp = float(stri[idx2 + 1:len(stri)-1])
    x_list.append(x_temp)
    y_list.append(y_temp)
    transformer = pyproj.Transformer.from_crs("epsg:2804", "epsg:4326", always_xy=True)
    # https://www.spatialreference.org/ref/?search=2804&srtext=Search
    # I used this to look up the projection with reference to Maryland coordinate system
    x2, y2 = transformer.transform(x_temp, y_temp)
    bus_list.append(stri[0:idx1])
    lon_list.append(x2)
    lat_list.append(y2)
    buscoord_lon_lat.append([stri[0:idx1], x2, y2])   # ans is (lon, lat)

# print(buscoord_lon_lat)

# Writing to an excel sheet using Python
# from xlwt import Workbook
#
# # Workbook is created
# wb = Workbook()
#
# # add_sheet is used to create sheet.
# sheet1 = wb.add_sheet('Bus coordinates')
#
# sheet1.write(0, 0, 'Bus_ID')
# sheet1.write(0, 1, 'Longitude')
# sheet1.write(0, 2, 'Latitude')
#
# for i in range(0, len(bus_list)):
#     sheet1.write(i+1, 0, bus_list[i])
#     sheet1.write(i+1, 1, lon_list[i])
#     sheet1.write(i+1, 2, lat_list[i])

# wb.save('Bus_coordinates_7732.xls')

## Writing to an CSV file using Python
import csv

with open('Bus_coordinates_7732.csv', mode='w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(['Bus_ID', 'Longitude', 'Latitude'])
    for i in range(0, len(bus_list)):
        writer.writerow([bus_list[i], lon_list[i], lat_list[i]])





#
# # Plotting on the USA map
#
# import matplotlib.pyplot as plt
# import geopandas as gpd
#
# # initialize an axis
# fig, ax = plt.subplots(figsize=(8,6))
#
# # plot map on axis
# countries = gpd.read_file(
#      gpd.datasets.get_path("naturalearth_lowres"))
#
# # countries.head()
# # countries.plot(color="lightgrey")
# countries[countries["name"] == "United States of America"].plot(color="lightgrey", ax=ax)
#
# for i in range(len(lon_list)):
#     plt.figure(1)
#     plt.scatter(lon_list[i], lat_list[i], marker="o", color='red', s = 4)
#     plt.xlabel('Longitude')
#     plt.ylabel('Latitude')
#     plt.show()
#
#
#
# # Plotting on Maryland map
# import geopandas as gpd
# import requests
# import zipfile
# import io
# import matplotlib
# matplotlib.use('TkAgg')
#
# url = 'https://www2.census.gov/geo/tiger/TIGER2016/COUSUB/tl_2016_24_cousub.zip'
# local_path = 'tmp/'
# print('Downloading shapefile...')
# r = requests.get(url)
# z = zipfile.ZipFile(io.BytesIO(r.content))
# print("Done")
# z.extractall(path=local_path) # extract to folder
# filenames = [y for y in sorted(z.namelist()) for ending in ['dbf', 'prj', 'shp', 'shx'] if y.endswith(ending)]
# print(filenames)
#
# dbf, prj, shp, shx = [filename for filename in filenames]
# usa = gpd.read_file(local_path + shp)
#
# ax = usa.plot()
#
# import matplotlib.pyplot as plt
# for i in range(len(lon_list)):
#     plt.figure(2)
#     plt.scatter(lon_list[i], lat_list[i], marker="o", color='red', s = 4)
#     plt.xlabel('Longitude')
#     plt.ylabel('Latitude')
#     plt.show()



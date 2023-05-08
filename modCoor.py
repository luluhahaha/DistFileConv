import pandas as pd
import numpy as np

coordf = pd.read_csv("Data/BGE/selected_10_feeders/Feeder_7893/Buscoords.dss",sep=' ', names=['Node','Lat','Lon'])
print(coordf)
#coordf = pd.read_csv("Data/BGE/selected_10_feeders/Feeder_7893/Buscoords.dss", sep='', header=None, names=['Node','Lat','Lon'] )

coordf['Lat'] = pd.to_numeric(coordf['Lat'])
coordf['Lon'] = pd.to_numeric(coordf['Lon'])


#outputfile = open("Data/BGE/selected_10_feeders/Feeder_7893/Buscoords_new.dss", "w")

coordf.loc[coordf['Lat'] > 440000, "Lat"] =  coordf['Lat']-61616.273 *0.9
coordf.loc[coordf['Lon'] > 190000, "Lon"] =  coordf['Lon']-31926.755 * 0.9

np.savetxt(r'Data/BGE/selected_10_feeders/Feeder_7893/Buscoords_new.dss', coordf.values, fmt='%s')



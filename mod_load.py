import re

# with open("Data/BGE/selected_10_feeders/Feeder_7731/Loads_37MW.dss", "r") as inputfile:
#     inputlines = inputfile.readlines()
# outputfile = open("Data/BGE/selected_10_feeders/Feeder_7731/Loads.dss", "w")
# load_scale = 5

with open("Data/BGE/selected_10_feeders/Feeder_7366/Loads_13MW.dss", "r") as inputfile:
    inputlines = inputfile.readlines()
outputfile = open("Data/BGE/selected_10_feeders/Feeder_7366/Loads.dss", "w")
load_scale = 1.6

for line in inputlines:
    if line.lower().startswith("new"):
        print("original:")
        print(line)
        kw = float(line.lower().split("kw=")[1].split(" ")[0])
        print("kw:" + str(kw))
        new_kw = kw/load_scale

        kvar = float(line.lower().split("kvar=")[1].split(" ")[0])
        new_kvar = kvar/load_scale


        newline = line.lower().split("kw=")[0] + "kw="+ str(new_kw) + " kvar=" + str(new_kvar) + " " + line.lower().split("kvar=")[1].split(" ")[1]
        print("mod:")
        print(newline)

        outputfile.write(newline)


outputfile.close()
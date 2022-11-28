# This file constructs a graph to show the connection of the feeder
# The main files used are the series elements consisting of the lines and transformers

with open('Lines.dss') as f:
    lines = f.readlines()

# print(type(lines))
# print(lines)

with open('Transformers.dss') as f:
    trafo = f.readlines()



se = []
re = []

for i in range(0, len(lines), 2):
    stri = lines[i]

    if stri[4:8] == 'Line':
        idx0 = stri.index('enabled=')
        if stri[idx0:idx0+9] == 'enabled=y':
            idx1 = stri.index('bus1') #index of bus 1
            idx2 = stri.index('bus2') #index of bus 2
            idx3 = stri.index('switch') #index of switch
            bus1_name = stri[idx1+5:idx2-1]
            bus2_name = stri[idx2+5:idx3-1]
            se.append(bus1_name)
            re.append(bus2_name)


non_sw_lines = []
nc_sw = []
no_sw = []
disa_lines = []

three_phs_lines = []
two_phs_lines = []
one_phs_lines = []

three_phs_nc_sw = []
two_phs_nc_sw = []
one_phs_nc_sw = []

three_phs_no_sw = []
two_phs_no_sw = []
one_phs_no_sw = []
for i in range(0, len(lines), 2):
    stri = lines[i]

    if stri[4:8] == 'Line':
        idx0 = stri.index('switch')
        if stri[idx0:idx0+18] == 'switch=n enabled=y': # all enabled non-switchable lines
            non_sw_lines.append(stri)
            temp = stri.index('phases')
            if stri[temp:temp + 8] == 'phases=3': # enabled 3-phase non-switchable lines
                three_phs_lines.append(stri)
            elif stri[temp:temp + 8] == 'phases=2': # enabled 2-phase non-switchable lines
                two_phs_lines.append(stri)
            elif stri[temp:temp + 8] == 'phases=1': # enabled 1-phase non-switchable lines
                one_phs_lines.append(stri)
            else:
                print('Go figure')

        elif stri[idx0:idx0+18] == 'switch=y enabled=y': # all enabled switches
            nc_sw.append(stri)
            temp = stri.index('phases')
            if stri[temp:temp + 8] == 'phases=3':  # enabled 3-phase non-switchable lines
                three_phs_nc_sw.append(stri)
            elif stri[temp:temp + 8] == 'phases=2':  # enabled 2-phase non-switchable lines
                two_phs_nc_sw.append(stri)
            elif stri[temp:temp + 8] == 'phases=1':  # enabled 1-phase non-switchable lines
                one_phs_nc_sw.append(stri)
            else:
                print('Go figure')

        elif stri[idx0:idx0 + 18] == 'switch=y enabled=n':  # all disabled switches
            no_sw.append(stri)
            temp = stri.index('phases')
            if stri[temp:temp + 8] == 'phases=3':  # enabled 3-phase non-switchable lines
                three_phs_no_sw.append(stri)
            elif stri[temp:temp + 8] == 'phases=2':  # enabled 2-phase non-switchable lines
                two_phs_no_sw.append(stri)
            elif stri[temp:temp + 8] == 'phases=1':  # enabled 1-phase non-switchable lines
                one_phs_no_sw.append(stri)
            else:
                print('Go figure')

        else:
            disa_lines.append(stri)



# Extracting the transformers' primary and secondary buses
for i in range(0, len(trafo), 2):
    stri = trafo[i]
    idx1 = stri.index('bus') #index of bus 1
    idx2 = stri.index('bus', idx1+1) #index of bus 2
    idx3 = stri.index('wdg=2') #index of winding
    idx4 = stri.index('XHL')  # index of winding
    bus1_name = stri[idx1+4:idx3-1]
    bus2_name = stri[idx2+4:idx4-1]
    se.append(bus1_name)
    re.append(bus2_name)



# Checking for duplicate series elements (in lines and trafo)
news = []
for i in range(len(se)):
    print(se[i], re[i])
    temp = [se[i], re[i]]
    news.append(temp)

unique_elements = [] # empty list to hold unique elements from the list
dup_elements = [] # empty list to hold the duplicate elements from the list
for i in news:
    if i not in unique_elements:
        unique_elements.append(i)
    else:
        dup_elements.append(i) # this method catches the first duplicate entries, and appends them to the list
# The next step is to print the duplicate entries, and the unique entries
print("List of duplicates", dup_elements)
print("Unique Item List", unique_elements) # prints the final list of unique items


# The goal is to plot the graph of all the buses
# Hence it is necessary to remove the phasing information i.e. '.1.2.3'
se_wo_phs = []
for s in se:
    length = len(s)

    if s[length - 12:] == '.1.2.3.1.2.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 11] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 12:] == '.1.2.3.3.1.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 11] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 12:] == '.1.2.3.2.1.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 11] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 12:] == '.3.1.2.1.2.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 11] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 12:] == '.2.1.3.1.2.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 11] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 6:] == '.1.2.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 6:] == '.1.3.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 6:] == '.3.2.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 6:] == '.3.1.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 6:] == '.2.3.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 6:] == '.2.1.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 5] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 4:] == '.1.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 4:] == '.1.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 4:] == '.1.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 4:] == '.2.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 4:] == '.2.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 4:] == '.2.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 4:] == '.3.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 4:] == '.3.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 4:] == '.3.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 3] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 2:] == '.1':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 1] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 2:] == '.2':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 1] + replacement
        se_wo_phs.append(res_str)

    elif s[length - 2:] == '.3':
        n = length - 1
        replacement = ''
        res_str = s[0:n - 1] + replacement
        se_wo_phs.append(res_str)

    else:
        se_wo_phs.append(s)



re_wo_phs = []
for r in re:
    length = len(r)

    if r[length - 12:] == '.1.2.3.1.2.3':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 11] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 12:] == '.1.2.3.3.1.2':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 11] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 12:] == '.1.2.3.2.1.3':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 11] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 12:] == '.3.1.2.1.2.3':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 11] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 12:] == '.2.1.3.1.2.3':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 11] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 6:] == '.1.2.3':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 5] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 6:] == '.1.3.2':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 5] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 6:] == '.3.2.1':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 5] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 6:] == '.3.1.2':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 5] + replacement
        re_wo_phs.append(res_str)


    elif r[length - 6:] == '.2.3.1':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 5] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 6:] == '.2.1.3':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 5] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 4:] == '.1.1':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 3] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 4:] == '.1.3':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 3] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 4:] == '.1.2':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 3] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 4:] == '.2.1':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 3] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 4:] == '.2.2':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 3] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 4:] == '.2.3':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 3] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 4:] == '.3.1':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 3] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 4:] == '.3.2':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 3] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 4:] == '.3.3':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 3] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 2:] == '.1':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 1] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 2:] == '.2':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 1] + replacement
        re_wo_phs.append(res_str)

    elif r[length - 2:] == '.3':
        n = length - 1
        replacement = ''
        res_str = r[0:n - 1] + replacement
        re_wo_phs.append(res_str)

    else:
        re_wo_phs.append(r)

# Now, I have removed all the phasing information from the series elements
# and can now proceed to plot the graph


# Plotting thee graph
import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

new = []
for i in range(len(re_wo_phs)):
    g.add_edge(se_wo_phs[i], re_wo_phs[i])
    print(se_wo_phs[i], re_wo_phs[i])
    temp = [se_wo_phs[i], re_wo_phs[i]]
    new.append(temp)

color_map = ['red' if node == 'SOURCE_7732' else 'green' for node in g]
size_map = [50 if node == 'SOURCE_7732' else 10 for node in g]
# nx.draw(g, with_labels = True)
nx.draw(g, node_size=size_map, node_color=color_map)
plt.show()

# nx.is_tree(g) # Check whether the graph is a tree
# nx.is_connected(g) # Check whether there is any isolated node



# ## Writing to an excel sheet using Python
# from xlwt import Workbook
#
# # Workbook is created
# wb = Workbook()
# # add_sheet is used to create sheet.
# sheet1 = wb.add_sheet('Node connections')
#
# sheet1.write(0, 0, 'From_node')
# sheet1.write(0, 1, 'To_node')
#
# for i in range(0, len(re_wo_phs)):
#     sheet1.write(i+1, 0, se_wo_phs[i])
#     sheet1.write(i+1, 1, re_wo_phs[i])
#
# wb.save('Node_connections_7732.xls')


## Writing to an CSV file using Python
import csv

with open('Node_connections_7732_wo_norm_open_sw.csv', mode='w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(['From_node', 'To_node'])
    for i in range(0, len(re_wo_phs)):
        writer.writerow([se_wo_phs[i], re_wo_phs[i]])





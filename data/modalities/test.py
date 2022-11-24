# importing module
from pandas import *

import json

# reading CSV file
data = read_csv("athlete_events.csv")

# converting column data to list
events = data['Event'].tolist()
noc = data['NOC'].tolist()
medal = data['Medal'].tolist()

# creating dictionary
dict = dict()


for i in range(len(events)):

    if events[i] not in dict:
        dict[events[i]] = {}

    if noc[i] not in dict[events[i]]:
        dict[events[i]][noc[i]] = {} 
        dict[events[i]][noc[i]]["nan"] = 0
        dict[events[i]][noc[i]]["Bronze"] = 0
        dict[events[i]][noc[i]]["Silver"] = 0
        dict[events[i]][noc[i]]["Gold"] = 0

    dict[events[i]][noc[i]][str(medal[i])] += 1


with open('demo.csv', 'w') as out:
    
    for key in dict:
        for key2 in dict[key]:

            out.write(key + "," + key2 + "," + str(dict[key][key2]["nan"]) + ","  + str(dict[key][key2]["Bronze"]) + "," + str(dict[key][key2]["Silver"]) + "," + str(dict[key][key2]["Gold"]) + "\n")





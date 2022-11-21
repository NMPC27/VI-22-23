# importing module
from pandas import *

# reading CSV file
data = read_csv("noc_regions.csv")

# converting column data to list
events = data['region'].tolist()#! ATENÇAO QUE NO ' O AUTOCOMPLETE NAO MOSTRA MAIS - nao posso apenas dar replace pq dps vou percisar de enviar isso ao pedro
# printing list data

dict = {}
for i in events:
    
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i in dict:
    if dict[i] > 1:
        print(i, dict[i])



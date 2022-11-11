# importing module
from pandas import *

# reading CSV file
data = read_csv("athlete_events.csv")

# converting column data to list
events = data['Event'].tolist()#! ATENÇAO QUE NO ' O AUTOCOMPLETE NAO MOSTRA MAIS - nao posso apenas dar replace pq dps vou percisar de enviar isso ao pedro
tmp=set(events)
# printing list data



print(tmp)


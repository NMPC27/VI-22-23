import csv
import copy


#females
# group,Nitrogen,normal,stress
# banana,12,1,13

dict = dict()

with open("males_medals.csv", 'r') as file:
  m = csv.reader(file)

  with open("females_medals.csv", 'r') as file2:
    f = csv.reader(file2)



    for row in m:
        if row == []:
            continue

        dict[row[0]] = {}

        dict[row[0]][row[1]] = {'medals': [row[2], row[3], row[4]]}

    for row in f:
        if row == []:
            continue
        
        if not row[0] in dict:
            dict[row[0]] = {}

        if not row[1] in dict[row[0]]:
            dict[row[0]][row[1]] = {'medals': [row[2], row[3], row[4]]}

        tmp=dict[row[0]][row[1]]['medals'] 
        print(tmp)
        dict[row[0]][row[1]]['medals'] = [int(tmp[0])+int(row[2]), int(tmp[1])+int(row[3]), int(tmp[2])+int(row[4])]



    print(dict)


    with open('all_medals.csv', 'w') as out:
        writer = csv.writer(out)


        writer.writerow(['event', 'country', 'bronze', 'silver', 'gold', 'all'])

        for key in dict:
            for key2 in dict[key]:

                writer.writerow([key, key2, dict[key][key2]['medals'][0], dict[key][key2]['medals'][1], dict[key][key2]['medals'][2]])



import csv
import copy


#females
# group,Nitrogen,normal,stress
# banana,12,1,13

dict = dict()

with open("females_by_event_bronze.csv", 'r') as file:
  bronze = csv.reader(file)

  with open("females_by_event_silver.csv", 'r') as file2:
    silver = csv.reader(file2)

    with open("females_by_event_gold.csv", 'r') as file3:
        gold = csv.reader(file3)

        for row in bronze:
            if row == []:
                continue

            dict[row[1]] = {}

            dict[row[1]][row[0]] = {}

            dict[row[1]][row[0]]["bronze"] = row[2]

        for row in silver:
            if row == []:
                continue
            
            if not row[1] in dict:
                dict[row[1]] = {}

            if not row[0] in dict[row[1]]:
                dict[row[1]][row[0]] = {}

            dict[row[1]][row[0]]["silver"] = row[2]

        for row in gold:
            if row == []:
                continue
            
            if not row[1] in dict:
                dict[row[1]] = {}

            if not row[0] in dict[row[1]]:
                dict[row[1]][row[0]] = {}

            dict[row[1]][row[0]]["gold"] = row[2]


        for key in dict:
            for key2 in dict[key]:

                if not "bronze" in dict[key][key2]:
                    dict[key][key2]['bronze'] = "0"

                if not "silver" in dict[key][key2]:
                    dict[key][key2]['silver'] = "0"
                
                if not "gold" in dict[key][key2]:
                    dict[key][key2]['gold'] = "0"

        print(dict)


        with open('females_medals.csv', 'w') as out:
            writer = csv.writer(out)


            writer.writerow(['event', 'country', 'bronze', 'silver', 'gold', 'all'])

            for key in dict:
                for key2 in dict[key]:

                    bronze=copy.deepcopy(dict[key][key2]['bronze'])
                    silver=copy.deepcopy(dict[key][key2]['silver'])
                    gold=copy.deepcopy(dict[key][key2]['gold'])


                    total = int(bronze) + int(silver) + int(gold)

                    writer.writerow([key, key2, dict[key][key2]['bronze'], dict[key][key2]['silver'], dict[key][key2]['gold']])



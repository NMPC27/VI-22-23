import csv

# get number of females with bronze medal from each country by each event in athletes_events.csv
# and write to females_by_event_bronze.csv

# open atheletes_events.csv
with open('athlete_events.csv', 'r') as atheletes_events:
    # open atheletes_by_country.csv
    # open atheletes_by_country.csv
    with open('females_by_event_bronze.csv', 'w') as atheletes_by_country:
        # create csv reader and writer
        reader = csv.reader(atheletes_events)
        writer = csv.writer(atheletes_by_country)
        # create empty dictionary
        atheletes_by_country_dict = {}
        # iterate over each row in atheletes_events.csv
        for row in reader:
            # get country name
            country = row[7]
            # get Games
            event = row[13]

            gender = row[2]

            medal = row[14]

            # if country is not in atheletes_by_country_dict
            if country != 'NOC':
                if country not in atheletes_by_country_dict:
                    # add country to atheletes_by_country_dict
                    atheletes_by_country_dict[country] = {}
                # if country is in atheletes_by_country_dict
                if event not in atheletes_by_country_dict[country] and gender == 'F' and medal == 'Bronze':
                    # add Games to atheletes_by_country_dict
                    atheletes_by_country_dict[country][event] = 1
                elif gender == 'F' and medal == 'Bronze':
                    # increment number of atheletes for that country
                    atheletes_by_country_dict[country][event] += 1
        # iterate over each key in atheletes_by_country_dict
        for key in atheletes_by_country_dict:
            # iterate over each key in atheletes_by_country_dict
            for event in atheletes_by_country_dict[key]:
                # write key and value to atheletes_by_country.csv
                writer.writerow([key, event, atheletes_by_country_dict[key][event]])

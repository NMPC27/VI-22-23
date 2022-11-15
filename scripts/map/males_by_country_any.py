import csv

# get number of males with any medal from each country by each Games in athletes_events.csv
# and write to males_by_country_any.csv

# open atheletes_events.csv
with open('athlete_events.csv', 'r') as atheletes_events:
    # open atheletes_by_country.csv
    # open atheletes_by_country.csv
    with open('males_by_country_any.csv', 'w') as atheletes_by_country:
        # create csv reader and writer
        reader = csv.reader(atheletes_events)
        writer = csv.writer(atheletes_by_country)

        writer.writerow(['code', 'games', 'participants'])

        # create empty dictionary
        atheletes_by_country_dict = {}
        # iterate over each row in atheletes_events.csv
        for row in reader:
            # get country name
            country = row[7]
            # get Games
            games = row[8]

            gender = row[2]

            medal = row[14]

            # if country is not in atheletes_by_country_dict
            if country != 'NOC':
                if country not in atheletes_by_country_dict:
                    # add country to atheletes_by_country_dict
                    atheletes_by_country_dict[country] = {}
                # if country is in atheletes_by_country_dict
                if games not in atheletes_by_country_dict[country] and gender == 'M' and medal != 'NA':
                    # add Games to atheletes_by_country_dict
                    atheletes_by_country_dict[country][games] = 1
                elif gender == 'M' and medal != 'NA':
                    # increment number of atheletes for that country
                    atheletes_by_country_dict[country][games] += 1
        # iterate over each key in atheletes_by_country_dict
        for key in atheletes_by_country_dict:
            # iterate over each key in atheletes_by_country_dict
            for games in atheletes_by_country_dict[key]:
                # write key and value to atheletes_by_country.csv
                writer.writerow([key, games, atheletes_by_country_dict[key][games]])

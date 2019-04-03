#!/usr/bin/env python3

import requests

# r = requests.get( 'http://api.open-notify.org/astros.json')
r = requests.get( 'http://api.open-notify.org/astros.json').json()

# helmetson =(r.json())


# print("Number of people in space: {}".format(helmetson["number"]))

for person in r["people"]:
    # print their names
    # list_names = person["name"].split()
    # print(list_names)

    list_names = person["name"].split()
    print(list_names)
    print(list_names[-1])



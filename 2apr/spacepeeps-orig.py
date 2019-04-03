#!/usr/bin/env python3

import urllib.request
import json

spaceweb = 'http://api.open-notify.org/astros.json'

groundctrl = urllib.request.urlopen(spaceweb)
print(dir(groundctrl))
print(groundctrl.headers)

helmet = groundctrl.read()
# print(helmet)

# look up "load" and "loads" methods
# if data has a little "be" in front, do the decode
helmetson = json.loads(helmet.decode('utf-8'))

print(helmetson)

print("Number of people in space: {}".format(helmetson["number"]))

for person in helmetson["people"]:
    # print their names
    list_names = person["name"].split()
    print(list_names)

    


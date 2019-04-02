#!/usr/bin/env python3
# pprint is prettyprint

import json
import pprint

with open("data.json") as json_file:
    data = json.load(json_file)
    pprint.pprint(data)
    for person_age in data["spaceship"]:
        print(person_age["age"])
        print(person_age["name"] + " is " + str(person_age["age"]) + " years old"
        print(person_age["name"] , "is", person_age["age"], "years old"
        print("{0} is {1} years old".format(person_age["name"] , "is", person_age["age"], "years old"




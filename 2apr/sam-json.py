#!/usr/bin/env python3
# pprint is prettyprint

import json
import pprint

with open("myjson.json") as json_file:
    data = json.load(json_file)
    pprint.pprint(data)



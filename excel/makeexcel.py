#!/usr/bin/env python3

import pyexcel

# Request data from user
def  get_ip_data():
    input_ip = input("\nWhat is the IP address?")
    input_driver = input("What is the driver associated with this device? ")
    d = {"IP": input_ip, "driver": input_driver}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets
## IP is the first column
##


# Runtime
mylistdict = []  # this will be our list we turn into a .xls file

print("Hello!  This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data())  # add an item to the list \
        # returned by get_ip_data() {"IP": value, "driver": value}
    keep_going = input("\nWould you like to add another value?  Enter \
                to continue, or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")

print("The file " + filename + ".xls should be in your local directory")

break

## reading from flat file
def get_ip_data():
    mylist = []
    with open("flat.txt", "r") as myfile:
        for row in myfile:
            myrow = row.split()
            d = {"IP": myrow[0], "driver": myrow[1], "port": myrow[3]}
            mylist.append(d)
    return mylist


print("Hello!  This program will make you a *.xls file")


#!/usr/bin/env python3

def main():
    # Read in our list data
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip:  # single line from our file is sline
            # append addes to the end of our list
            # rstrip removes any special characters on the right of the str
            # split breaaaks our string into a list
            # the result is we add a list of drivers and ip's to networklists
            networklists.append(sline.rstrip("\n").split(' '))

            print(networklists) # display networklists to ensure we recreated

            for driveandip in networklists:
                print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()


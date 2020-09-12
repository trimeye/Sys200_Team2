#!/usr/bin/python3

import hashlib
import logging
import getpass
import passlib

#DEBUG Detailed information, typically of interest only when diagnosing problems.
#INFO Confirmation that things are working as expected.
#WARNING An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). still working as expected. **default setting**
#ERROR Due to a more serious problem, the software has not been able to perform some function.
#CRITICAL A serious error, indicating that the program itself may be unable to continue running.
#make a readme file

logging.basicConfig(filename="logging.log",filemode="a",format="%(asctime)s:%(levelname)s:%(message)s",level=logging.DEBUG)

loginDict={"root":"toor","mav":"maverick","roger":"dodger"}

for attempt in range (5,0,-1):
    username = input("Please enter your username: ")
    password = getpass.getpass()
    
    if loginDict.get(username) and loginDict[username] == password:
        print("Welcome!")
        break  # or use exit() ???

    elif attempt >= 2:
        print("Invalid Access Attempt")
        print("You have", str(attempt-1), "attempts left.")
        logging.debug("Unknown person attempted to login with invalid username.")

    else:
        print("You have run out of log in attempts.")
        logging.debug("User: " + username + "locked out at #timedate.")                      

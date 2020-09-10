#!/usr/bin/python3
#Login_Team2
import hashlib
import logging
import getpass
 
logging.basicConfig(filename="myFirstLog.log", filemode="a", format="%(levelname)s:%(message)s",  level=logging.WARNING)

x = 5
 
pwlist = {}
with open ("/home/17192/Desktop/python things/hashedFile.txt") as pfile:
    for line in pfile:
         user, pw = line.partition(":")[::2]
         pwlist[user.strip()] = pw
 
    while(x >= 1):
     usernameprompt = input("Please Enter Username: ")
    if(usernameprompt in pwlist.keys()):

        passwordprompt = input("Please Enter Password: ")
        pwhash = (hashlib.sha256(passwordprompt.encode()).hexdigest())
        
    if(pwhash in pwlist[usernameprompt]):
        print("Welcome!")
        break
    else:
        print("Invalid Password")
        #print("You have", str(x), "attempts left.")
          logging.warning(usernameprompt + " attempted to login with the wrong password")
    else:
        print("Invalid Username")
          x = x - 1
        print("You have", str(x), "attempts left.")
          logging.warning("Unknown person attempted to login with invalid username.")
    if(x < 1):
        print("You have run out of log in attempts.")
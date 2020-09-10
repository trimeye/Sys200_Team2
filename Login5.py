
import hashlib
import logging
from typing import Dict, Any

logging.basicConfig(filename="logging.log", filemode="a", format="%(levelname)s:%(message)s",  level=logging.WARNING)
#loginDict = {"User1" : "User1pass", "User2" : "User2pass", "User3" : "User3pass"}
#username = ["User1", "User2", "User3"]
#password = ["User1pass", "User2pass", "User3pass"]
i = 5
pwlist: Dict[Any, Any] = {}
with open("/home/samann/Desktop/Textfiles/user_hash.txt") as pfile:
    for line in pfile:
        user, pw = line.partition(":")[::2]
        pwlist[user.strip()] = pw
while(i >= 1):
    usernameprompt = input("Please Enter Username: ")
    if(usernameprompt in pwlist.keys()):
#       passwordprompt = getpass.getpass("Please Enter Password: ")
          passwordprompt = input("Please Enter Password: ")
          pwhash = (hashlib.sha256(passwordprompt.encode()).hexdigest())
#       if(passwordprompt in loginDict):
          if(pwhash in pwlist[usernameprompt]):
              print("Welcome!")
              break
          else:
              print("Invalid Password")
              i = i - 1
              print("You have", str(i), "attempts left.")
              logging.warning(usernameprompt + " attempted to login with the wrong password")
    else:
        print("Invalid Username")
        i = i - 1
        print("You have", str(i), "attempts left.")
        logging.warning("Unknown person attempted to login with invalid username.")
if(i < 1):
      print("You have run out of log in attempts.")
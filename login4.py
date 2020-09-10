#!/usr/bin/python3
#start a for loop to track attempts
#ask input from user for their username and password
#use getpass to cloak password entry
#check these inputs against dictionary key and value
#if inputs are in loginDictionary, grant access to system
#if not, display error message to try again with 5 attempts max
#countdown attempts remaining with increment -1
#user reaches no attempts, login terminates
#stackOverflow to the rescue!

from getpass import getpass

loginDict = {"root":"toor", "mav":"maverick", "roger":"dodger"}
#print(loginDict)
#print( "you entered", p )
for i in range (5,0, -1):
    x = input("Who are you? What is your username?" )
    p = getpass()
    #print(i) 
    if loginDict.get(x) and loginDict[x] == p:
        print("access GRANTED!!!")
        #print(i)
        exit()
    elif i != 1:
        print("something is not correct, try again", i-1 , "attempts left")
    else:
        print("too many attempts, access denied, goodbye")



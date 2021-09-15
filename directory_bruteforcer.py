#!/usr/bin/env python
#
#
#   Need to add threads
#
#



import requests

url = input("Pick a url: ")
extensions = input("any extensions???") # fix extensions module

with open("/opt/small.txt","r") as h:
    h = [ line for line in h.read().split("\n") if line]
for x in h:
    if extensions == "":
        #this code is bad
        response = requests.get("http://" + url + "/",x)
    else:
        #this code is bad
        response = requests.get("http://" + url + "/",x + "."+extensions) 
    #need to find a better print format
    print (x, ":", response)

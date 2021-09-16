#!/usr/bin/env python
import threading
import requests
import argparse
import sys
url = sys.argv[1]
wordlist = sys.argv[2]
extensions = sys.argv[3]



print("----------------------------------------------------------")
print("----------------------------------------------------------")
print("----------------------------------------------------------")
print("----------------------------------------------------------")
print("bruteforcing this url:"+"           "+"["+url+"]")
print("----------------------------------------------------------")
print("with this extension:"+"             "+"["+extensions+"]")
print("----------------------------------------------------------")
print("with this wordlist:"+"              "+"["+wordlist+"]")
print("----------------------------------------------------------")
print("\n \n \n \n") 


with open(wordlist,"r") as h:
    h = [ line for line in h.read().split("\n") if line]
for x in h:
    
    response = requests.get("http://" + url + "/",x + "."+extensions) 
    
    
    print ("/"+x, ":", response)
  
        


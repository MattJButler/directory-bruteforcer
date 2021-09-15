import requests
import os
url = input("Pick a url: ")
r = requests.get("http://"+url)


with open(director, "r") as h
    directories = [ line.strip for line in h.read().split("\n") if line]
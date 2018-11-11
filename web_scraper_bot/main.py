#PYTHON 2 & 3 CROSS COMPATIBILITY SUPPORT
from __future__ import (absolute_import, division, print_function, unicode_literals)

import requests
import timeit
from bs4 import BeautifulSoup #BS Web Scraper kit
# import re #Regular Expressions

start_time = timeit.default_timer() #start timer

#MALICIOUS_COMPLY
malicious_comply = requests.get("https://www.reddit.com/r/MaliciousCompliance/")

fetch = BeautifulSoup(malicious_comply.content, "html5lib")   #Check webpage for tags found
print("\n<<<<<MALICIOUS COMPLIANCE>>>>>>")
print(fetch)

#Time taken for module to run
stop_time = timeit.default_timer()
elapsed_time_secs = stop_time - start_time
print("PROGRAM EXECUTED IN")
print(round(elapsed_time_secs, 3), end="")
print(" seconds")



# #TALES_FROM_TECH_SUPPORT
# tales_tech = requests.get("https://www.reddit.com/r/talesfromtechsupport/")  # ACCESS WEBSITE
#
# fetch2 = BeautifulSoup(tales_tech.content, "html5lib")  # Check webpage for tags found
# print("\n<<<<<TALES FROM TECH SUPPORT>>>>>s")
# print(fetch2)



    # tags = fetch.findAll("img", {"src": re.compile("\.\./uploads/photo_.*\.jpg")})
    # tags2 = fetch.findAll("img", {"src": re.compile("\.\./uploads/photo_.*\.gif")})
    # tags3 = fetch.findAll("img", {"src": re.compile("\.\./uploads/photo_.*\.png")})



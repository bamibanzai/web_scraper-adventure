#PYTHON 2 & 3 CROSS COMPATIBILITY SUPPORT
from __future__ import (absolute_import, division, print_function, unicode_literals)
import timeit
import duckduckSearch
#import scrapy


start_time = timeit.default_timer() #start timer

question = duckduckSearch.query('DuckDuckGo')



#Time taken for module to run
stop_time = timeit.default_timer()
elapsed_time_secs = stop_time - start_time
print("PROGRAM EXECUTED IN")
print(round(elapsed_time_secs, 3), end="")
print(" seconds")

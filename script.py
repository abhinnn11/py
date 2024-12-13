import requests
import random
from bs4 import BeautifulSoup
import csv
import os
import time
def calculate_home_disk_usage():
    total_size = 0
    home_dir = "/home/all/test"
    for dirpath, dirnames, filename in os.walk(home_dir):
        for f in filename:
            fp = os.path.join(dirpath, f)
            if  not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return round(total_size / (1024*1024), 2)


home_disk_usage = calculate_home_disk_usage()
print (home_disk_usage)

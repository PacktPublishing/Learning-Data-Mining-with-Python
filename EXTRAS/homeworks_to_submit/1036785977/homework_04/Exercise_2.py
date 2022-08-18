# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 16:17:39 2022

@author: Santiago Ruiz

Exercise 2
Make a live plot (refreshed every 1 second) of the growth of the world population using web-scrapping technique
https://countrymeters.info/en/World (or from any other website that uses a similar counter)
(use command line and terminal)

python3 plot_population.py --current_population
"""

import sys
import re
from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
import os
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import scipy.stats as stats
import random



def population(i):
  
  page  = requests.get("https://countrymeters.info/en/World")
  soup = BeautifulSoup(page.content, 'html.parser')  
  val = soup.find_all("div",  attrs={"id": "cp1"})
  num = re.findall(r'(\d+),(\d+),(\d+),(\d+)',str(val))
  num = num[0][0] + num[0][1] + num[0][2] + num[0][3]

  return int(num)

x=[]
y=[]

i=0

def update_plot(j): 

    global i,latency,sample
    i=i+1
    response=population(i)
    y.append(float(response))
    x.append(float(i))
    
    ax.plot(x,y,'-k')
    ax.grid(True)
    ax.set_xlabel('time')
    ax.set_ylabel('ping') 

fig,ax = plt.subplots(1,1,figsize=(5.4,3.3))
animation = animation.FuncAnimation(fig, update_plot, repeat=False, interval=1000)
plt.show()


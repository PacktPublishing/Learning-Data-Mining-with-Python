"""
Exercise 2
Make a live plot (refreshed every 1 second) of the growth of the world population using web-scrapping technique
https://countrymeters.info/en/World (or from any other website that uses a similar counter)
(use command line and terminal)
python3 plot_population.py --current_population
"""

import requests
import re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

#%matplotlib notebook
import time

def World_population(path="https://countrymeters.info/en/World"):
    page = requests.get(path)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    return int(soup.find('div', id='cp1').text.replace(',',''))

x=[]
y=[]
i=0

def live_plot(j): 

    global i,latency,sample
    i=i+1
    y.append(World_population())
    x.append(i)

    ax.plot(x,y,'-k')
    ax.grid(True)
    ax.set_xlabel('time [seg]')
    ax.set_ylabel('Current population') 

fig,ax = plt.subplots(1,1,figsize=(5.4,3.3))
animation = animation.FuncAnimation(fig,
                                    live_plot, 
                                    repeat=False, 
                                    interval=1000) #interval is time between frames in miliseconds
plt.show()


#if __name__ == '__main__':
#  main()

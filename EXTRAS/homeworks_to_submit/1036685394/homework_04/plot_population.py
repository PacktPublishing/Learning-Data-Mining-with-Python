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


def current_pop():
    
    page = requests.get("https://countrymeters.info/en/World")
    soup = BeautifulSoup(page.content, "html.parser")

    info = soup.select('td div[id="cp1"]')
    current_pop_n = re.findall(r'>(.+)<',str(info[0]))[0]
    
    return  int(current_pop_n.replace(',','')) 


x=[]
y=[]

i=0

def update_plot(j): 

    global i,latency,sample
    i=i+1
    y.append(current_pop())
    x.append(i)
    
    ax.plot(x,y,'-k')
    ax.grid(True)
    ax.set_xlabel('time')
    ax.set_ylabel('current_population') 
    
    

fig,ax = plt.subplots(1,1,figsize=(5.4,3.3))
animation = animation.FuncAnimation(fig, update_plot, repeat=False, interval=1000) #interval is time between frames in miliseconds
plt.show()

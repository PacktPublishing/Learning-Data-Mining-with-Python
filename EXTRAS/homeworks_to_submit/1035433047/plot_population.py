import sys
import time
import random
import requests
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from matplotlib.animation import FuncAnimation

fig,ax = plt.subplots(1,1,figsize=(5.4,3.3))
def population_number(link):
    page=requests.get(link)
    soup=BeautifulSoup(page.content,'html.parser')
    population=float(soup.select('td div[id="cp1"]')[0].get_text().replace(",",""))
    return population

x=[]
y=[]

def update_plot(j):
    ax.cla()
    y.append(population_number("https://countrymeters.info/en/World"))
    Date=[str(datetime.now().hour),':',str(datetime.now().minute),':',str(datetime.now().second)]
    x.append("".join(Date))
    ax.plot(x,y,'-o')
    ax.set_title('World Population Growth')
    ax.set_xlabel('Time')
    ax.set_ylabel('Population Current') 


animation = FuncAnimation(fig, update_plot, repeat=False, interval=1000)
plt.show()


def main():
    args=sys.argv[1:]
    if args[0]=='--current_population':
        FuncAnimation(fig, update_plot, repeat=False, interval=1000)
        

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# coding: utf-8
#Elaborated by: Joseph Nicolay RA

from requests import get
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep
import os
import sys

def get_info(url = "https://countrymeters.info/en/World"):    
    page = get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    counter = soup.select("td.counter div[id=cp1]")[0].text
    counter_name = soup.select('td.data_name b')[0].text
    return counter_name, int(counter.replace(',',''))

x=[]
y=[]
i=0   
def main():    
    args = sys.argv[1:]
    
    if args[0]=='--current_population':
        del args[0]

        def update_plot(j): 
            global i,latency,sample
            i+=1
            data_capture = get_info()   
            y.append(data_capture[1])
            x.append(i)
            
            ax.grid(True)
            ax.set_title(data_capture[0])
            ax.set_xlabel('Time Window')
            ax.set_ylabel('Number of habitants')
            ax.plot(x,y,'s-k')

        fig,ax = plt.subplots(1,1,figsize=(5.4,3.3))
        anim = animation.FuncAnimation(fig, update_plot, repeat=True, interval=1000)
        plt.show()
        
if __name__ == '__main__': 
    main()


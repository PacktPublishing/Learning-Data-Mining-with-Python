#!/usr/bin/python

import os
import sys
import re
import time
import numpy as np
from sympy import arg
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.offsetbox import AnchoredText
import datetime
import requests
import scipy.stats as stats
import random

def extract_current_population(url):
    '''
    Funcion que permite extraer la "Current Population" de la url.
    el resultado lo entrega en un integer.
    '''
    wp = requests.get(url)
    wp.status_code
    soup_wp = BeautifulSoup(wp.content, 'html.parser')
    pick_stocks = soup_wp.select("table td.counter")
    regex = r'"cp1">(\d+.*\d)'
    temp_val = re.findall(regex,str(pick_stocks[0]))[0]
    temp_val = temp_val.replace(",","")
    return int(temp_val)

def main():
    '''
    Si python3 plot_population.py --current_population: Imprime en terminal el la Current population y el tiempo en que fue adquirido
    el dato, ademas grafica en tiempo real estos datos.
    '''
    
    args = sys.argv[1:]

    if not args:
        print('usage: [--current_population] file [file ...]')
        sys.exit(1)

    flag = False
    if args[0] == '--current_population':
        global animation
        flag = True

        x = []
        y = []
        
        def update_plot(j): 
            url = "https://countrymeters.info/en/World"
            now = datetime.datetime.now()
            
            x.append(str(now.time()).split(".")[0])
            y.append(extract_current_population(url))
            print(x[-1],y[-1])
            
            ax.plot(x,y,"o",color="black")
            ax.plot(x,y,"--",color="b")
            ax.fill_between(x,y,y[0],color="skyblue")
            #ax.grid()

            population = AnchoredText("Current population: {}".format(y[-1]), loc=2)
            time = AnchoredText("Current time: {}".format(x[-1]), loc=4)
            ax.add_artist(population)
            ax.add_artist(time)

            ax.set_xlabel('time')
            ax.set_ylabel('Current population')

        fig,ax = plt.subplots(1,1,figsize=(5.4,3.3))
        animation = animation.FuncAnimation(fig, update_plot, repeat=False, interval=1000)
        plt.show()
        

if __name__ == '__main__':
    main()

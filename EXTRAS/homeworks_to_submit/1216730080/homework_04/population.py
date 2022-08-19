import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.animation import FuncAnimation # FuncAnimation is a class in matplotlib animation module
from IPython import display
from bs4 import BeautifulSoup
import requests
import numpy as np

def population(url='https://countrymeters.info/en/World'):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    tag = soup.find('div', id='cp1').text
    tag = int(tag.replace(',',''))
    return tag

def animate(i):
  
    x = 3*i # assigning 'Time' column to x variable
    y = population() # assigning 'HRR' column to y variable
    
    plt.plot(x, y,  'ro', label = 'HRR') # selecting the x and y variables to plot
    plt.ylim(y-100,y+100)
    #plt.xlim(x-5, x+5)
    plt.xlabel('Time (s)') # label x axis
    plt.ylabel('Population') # label y axis
    plt.title('World Population Live.') 

ani = FuncAnimation(plt.gcf(), animate, interval = 1000, frames = 500, repeat = False)


plt.tight_layout() # adds padding to the graph
plt.show() # show graph
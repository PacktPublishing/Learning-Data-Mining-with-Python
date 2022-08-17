#Homework4-Part2-Nicolas Echeverri Rojas

#Este codigo grafica en tiempo real el crecimiento poblacional mundial
#usando web-scrapping

# ejecutar como: C:/Users/nico0/anaconda3/python.exe plot_population.py --current_population


import sys 
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from bs4 import BeautifulSoup
import time
import requests


import matplotlib
font = {'size'   : 16, 'family':'STIXGeneral'}
axislabelfontsize='large'
matplotlib.rc('font', **font)

def read_population():
    page=requests.get('https://countrymeters.info/en/World')
    soup=BeautifulSoup(page.content,'html.parser')
    
    population=int(soup.select('td')[0].get_text().replace(",",""))
    return population

def update_plot(j): 
    global i
    i=i+1

    population=read_population()
    population_list.append(population )
    frame_list.append(i)

    ax.plot(frame_list,population_list,'-', color='#c501e2')
    ax.grid(True)
    ax.set_xlabel('time [s]')
    ax.set_ylabel('Population growth') 


def main():
  global i, fig,ax, population_list, frame_list

  i=0
  args = sys.argv[1:]
  
  #el método de sys argv obtiene los argumentos que se pasan por terminal
  #se empieza en el segundo elemento para que no tome el nombre 

  if not args:
    print('usage: [--current_population] for a live plot of population growth')
    #Imprime este mensaje si no se suministró argumentos
    sys.exit(1)

  if args[0]=='--current_population':
        print("--current_population enabled")
  
        population_list=[]
        frame_list=[]

        fig,ax = plt.subplots(1,1,figsize=(5.4,3.3))
        animation1 = animation.FuncAnimation(fig, update_plot, repeat=False, interval=1000)
        plt.show()


if __name__ == '__main__':
  main()
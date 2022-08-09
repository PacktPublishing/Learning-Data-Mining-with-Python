#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

def extract_info():
    #Se usa BeautifulSoup para obtener el valor de población y se convierte en entero
    url = 'https://countrymeters.info/en/World'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    cp = soup.select('div[id=cp1]')[0].get_text()
    return int(cp.replace(',',''))


def main():
    #Se activa el modo interactivo en la graficación
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1) 
    
    #Se hace un ciclo for para graficar en cada segundo el nuevo dato de población obtendio
    for i in range(100):
        b = extract_info()
        ax.set_xlim(-1, 100)
        ax.plot(i, b,'mo')
        display(fig)
        clear_output(wait = True)
        plt.xlabel('Time (s)')
        plt.ylabel('Current population')
        plt.pause(0.1)
  
if __name__ == '__main__':
  main()

from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
Time = []
Population = []

def extractPopulation():
    
    # Url of the website 
    url = "https://countrymeters.info/en/World"
    web = requests.get(url)
    # BeautifulSoup of the url
    soup = BeautifulSoup(web.content, 'html.parser')
    
    # Extracting the world live population
    population = soup.select('tr div[id=cp1]')
    # Text of the world population
    pop = population[0].get_text()
    # Replacing the ',' with ''
    pop = re.sub(',', '', pop)
    # Converting to float
    float_pop = float(pop)
    
    return float_pop

# Function to plottinf the live graphic
def animate(i):
    
    # List with the seconds
    Time.append(i)
    # Population list with the live population every second
    Population.append(extractPopulation())
    
    ax1.clear()
    # Plotting
    ax1.plot(Time, Population)
    
    plt.xlabel('Time (s)') 
    plt.ylabel('Population') 
    plt.title('World Population Live') 
    

def main():
    
    args = sys.argv[1:]
   
    if not args:
        print('usage: [--current_population] file [file ...]')
        sys.exit(1)
       
    flag = False
    if args[0] == '--current_population':
        flag = True
        del args[0]
        
    if flag:
        
        # Plotting the animation every second with interval=1000 miliseconds = 1 second
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        # Plot
        plt.show()
    
    else:
        print('usage: [--current_population] file [file ...]')

          
if __name__ == '__main__':
    main()
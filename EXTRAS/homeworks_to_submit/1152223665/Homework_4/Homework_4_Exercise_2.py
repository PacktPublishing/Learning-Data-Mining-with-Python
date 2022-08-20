import sys
import requests
from bs4 import BeautifulSoup
from time import process_time
import matplotlib.pyplot as plt
import matplotlib
#%matplotlib qt
matplotlib.use('Qt5Agg')

def Scrap_Population():
    Link_inicial = "https://countrymeters.info/en/World"
    Page_inicial  = requests.get(Link_inicial) #for access to web page 
    soup = BeautifulSoup(Page_inicial.content, 'html.parser') #for convert the web page in a soup 
    html_currente_population = soup.select("td.counter div") #for select the tag of html for access to specific places of web page
    x=html_currente_population[0].text 
    return int(x.replace(",",""))

def Plot_Population():
    
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--current_population] ')
        sys.exit(1)
        

    # Notice the summary flag and remove it from args if it is present.
    if args[0] == '--current_population':
    
        i=0
        pop=[]
        seg=[]
    
        pop.append(Scrap_Population())
        seg.append(0)
        print(i+1," Elapsed time in seconds between measures of population:", seg[i], "Population: ", pop[i])
        
        plt.title("Current World Population vs Time [s]")
        plt.xlabel("Time [s]")
        plt.ylabel("Current World Population")
        while True:
            i+=1
            start = process_time() 
            pop.append(Scrap_Population())
            end = process_time()
            slep=end-start
            seg.append(seg[i-1]+slep)
            print(i+1," Elapsed time in seconds between measures of population:", slep, "Population: ", pop[i])
            plt.plot([seg[i-1],seg[i]],[pop[i-1],pop[i]],"k-")
            plt.pause(1e-2)
        plt.show()
            
if __name__ == '__main__':
    Plot_Population()
    
    
    
    
    
    
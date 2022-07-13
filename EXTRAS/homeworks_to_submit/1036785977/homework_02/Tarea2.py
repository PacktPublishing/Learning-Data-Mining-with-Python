# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:17:39 2022

@author: Santiago Ruiz
"""

import sys
import re
import pandas as pd

"""Baby Names exercise
Define the extract_names() function below and change main()
to call it.
For writing regex, it's nice to include a copy of the target
text for inspiration.
Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
- Get the names data into a dict and print it (you can skip the dictionary and directly use lists if you prefer)
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  archivo = open(filename,"r")
  archivo = archivo.read()
  
  año = re.findall(r"in+\s+(\d{4}).",archivo) # extrae el año
  
  lista = re.findall(r"><td>+(\d{1,}).",archivo) # Extrae la posicion de los nombres
  
  nombres = re.findall(r"td><td>+(\w{1,})+<",archivo) # Extrae los nombres (mujeres y hombres)
  
  # Dividimos entre hombres y mujeres
  hombres = [] 
  mujeres = []
  
  for i in range(0,len(nombres)):
      if i==0:
          hombres.append(nombres[i])
      elif (i%2)==0:
          hombres.append(nombres[i])
      else:
          mujeres.append(nombres[i])
  
  # resultados deseados
  resultado = []
  for i in range(0,len(lista)): 
      a = hombres[i]+" "+lista[i]
      resultado.append(a)
      
  for i in range(0,len(lista)): 
      a = mujeres[i]+" "+lista[i]
      resultado.append(a)   
  
  resultado.sort()
  
  #añadimos el año
  resultado.insert(0, año[0])
  
  return resultado


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  pandFinal = pd.DataFrame()
  for i in args:
    resultado = extract_names(i)
    text = '\n'.join(resultado) + '\n'
    
    pand = pd.DataFrame(resultado[1:],columns=[resultado[0]])
    pandFinal = pd.concat([pandFinal,pand],axis=1)
    
    new = i+".summary"
    newfile = open(new,"w")
    newfile.write(text)
    newfile.close()
  
  pandFinal.to_csv("Resultados")
    
  
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  # create Pandas DataFrame with columns being the years and rows being alphabetically listed names 
  # save the frame into CSV file
  
if __name__ == '__main__':
  main()

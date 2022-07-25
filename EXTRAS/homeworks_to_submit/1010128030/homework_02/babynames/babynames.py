#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


import sys
import re
import numpy as np
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
  # +++your code here+++
  
  #Open and read HTML file
  HtmlFile = open(filename, 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  
  #Extract year and names of every document
  lista = re.findall(r"Popularity in (\d{4})", source_code)
  nombres = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', source_code)
  
  #Organize information as desired
  for i in range(len(nombres)):
    lista.append(nombres[i][1] + ' ' + nombres[i][0])
    lista.append(nombres[i][2] + ' ' + nombres[i][0])
  lista.sort()
  
  return lista


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

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  # create Pandas DataFrame with columns being the years and rows being alphabetically listed names 
  # save the frame into CSV file
  
  #Empy lists for pandas DataFrame
  col = []
  rows = []
  
  #For loop to print all of user requirements
  for i in args:
      
    #Use the function extract_names
    lista = extract_names(str(i))
    
    #Fill the lists
    col.append(lista[0])
    rows.append(lista[1:])
    
    #Organize the text for beauty print
    text = '\n'.join(lista) + '\n'
    
    if summary == True:
        with open(str(i) + '.summary','w') as f: # abrir documento para escribir (write: 'w') como un alias "f" 
            for palabra in lista:
                f.write(palabra+'\n') 
    else:
        print(text)

  #Create DataFrame and transform into CSV file.
  rows=np.array(rows).transpose()
  df=pd.DataFrame(data=rows, columns=col)
  df.to_csv("Babynames_by_year.csv")
  
if __name__ == '__main__':
  main()

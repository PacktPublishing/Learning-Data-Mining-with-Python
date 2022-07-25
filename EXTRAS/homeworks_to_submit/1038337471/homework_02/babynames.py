#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


import re
import codecs
import sys
import pandas as pd

#archivo=open("baby1990.html")
#file = codecs.open("baby1990.html", 'r', "utf-8") 
#filename=file.read()
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

def extract_names(archivo,Y):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  indices = re.findall(r"<td>(\d+)</td>", archivo)
  hombres = re.findall(r"<td>(\D+)</td><td>", archivo)
  mujeres = re.findall(r"\D</td><td>(\D+)</td>\n", archivo)

  #print(indices)
  #print("#####################################################")
  #print(hombres)
  #print("#####################################################")
  #print(mujeres)

  todos=hombres+mujeres
  todos.sort()

  extraeNombre=[Y]

  for item in todos:
    #if item not in extraeNombre:
    if (item in hombres) and (item not in mujeres):
      extraeNombre.append([item+" "+str(hombres.index(item)+1)])
    if (item in mujeres) and (item not in hombres):
      extraeNombre.append([item+" "+str(mujeres.index(item)+1)])

    if (item in mujeres) and (item in hombres):
      if hombres.index(item)<=mujeres.index(item):
        extraeNombre.append([item+" "+str(hombres.index(item)+1)])
      else:
        extraeNombre.append([item+" "+str(mujeres.index(item)+1)])

    #if (item in hombres) and (item in mujeres):
      #print(item)
  # +++your code here+++
  return extraeNombre, len(extraeNombre)


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  
  babyYear=["baby1990.html","baby1992.html","baby1994.html", "baby1996.html","baby1998.html","baby2000.html","baby2002.html","baby2004.html","baby2006.html","baby2008.html"]
  tablaDatos={}
  for year in babyYear:
    l=[]
    archivo=open(year)
    file = codecs.open(year, 'r', "utf-8") 
    filename=file.read()

    J=re.findall(r"y(\d+).", year)

    listas,n=extract_names(filename, J)
    for nombre in listas:
      l.append(nombre[0])
    #print(l)

    tablaDatos[J[0]]=l
    del tablaDatos[J[0]][0]
    
  df=pd.DataFrame(tablaDatos)
  df.to_csv("babynames.csv")
  df=pd.read_csv("babynames.csv")
  df=df.drop(["Unnamed: 0"],axis=1)
  
  
  
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
  
if __name__ == '__main__':
  main()

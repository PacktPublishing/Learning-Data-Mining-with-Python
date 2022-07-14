#!/usr/bin/python

import sys
import re
import os
import pandas as pd
from sympy import arg

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

  '''
  adsf
  '''
  year = []
  data = []
  dict_list = []
  male = []
  female = []

  with open(filename,'r') as f:
      html_string = f.read()

  list_rawstrings = html_string.split('\n')
  for i in list_rawstrings:
      temp_yearh3 = re.findall(r'(\d+)</h3>', i)
      temp_yearh2 = re.findall(r'(\d+)</h2>', i)
      if len(temp_yearh3) != 0:
          year.append(temp_yearh3[0])
      if len(temp_yearh2) != 0:
          year.append(temp_yearh2[0])
      temp_data = re.findall(r'<td>(\w+)</td>', i)
      if len(temp_data) != 0:
          data.append(temp_data)

  all_data = year + data

  for i in range(len(all_data)-1):
      dict_names = {'year':all_data[0],'name rank':all_data[i+1][0],
                  'male name':all_data[i+1][1],'female name':all_data[i+1][2]}
      dict_list.append(dict_names)

  for i in dict_list:
      male.append(str(i['male name']+" "+i['name rank']))
      female.append(str(i['female name']+" "+i['name rank']))

  temp_list = male + female
  sorted_list = year+sorted(temp_list, key=str.lower)

  text = '\n'.join(sorted_list)+'\n'
  
  return text
    
def createDataFrame(folders):
  data = []
  years = []
  for i in folders:
    names = extract_names(i).split("\n")[1:-1]
    year = extract_names(i).split("\n")[0]
    data.append(names)
    years.append(year)
  d = dict(zip(years,data))
  df = pd.DataFrame(data=d)
  print(df)
  return df


def main():
 
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile' and (len(args) > 1):
    summary = True
    del args[0]
    df = createDataFrame([args[0]])
    df.to_csv("{}summaryNames.csv".format(df.columns[0]),index=None)
    #print("Creando el documento ...", end="")
    print("Se ha creado el summary del archivo {} en el siguiente path:\n \t ---| {}\{}summaryNames.csv".format(str(args[0]),sys.path[0],df.columns[0]))

  elif (args[0] == '--summaryfolder') and (len(args) == 1):
    html_folder = [ x for x in os.listdir() if (x.split(".")[1] == 'html')]
    args[0] = html_folder
    df = createDataFrame(args[0])
    df.to_csv("summaryDataFrame.csv",index=None)
    print("Se ha creado el summary del folder en el siguiente path:\n \t ---| {}".format(sys.path[0]+"\summaryDataFrame.csv"))

  else:
    names = extract_names(args[0])
    print("Imprimiendo los primeros 10 resultados: \n")
    print(names[:110]+"\n.\n..\n...\n")
    print("No se han guardado los datos en ninguna summary file. Indique '--summaryfile' si desea guardar este texto o")
    print("'--summaryfolder' si desea guardar este resultado junto con todos los html file de la carpeta.")

  
if __name__ == '__main__':
  main()

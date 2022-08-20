#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


import sys
import re
import io
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
    
  file = open(filename, "r")
  strFile = file.read()
    
  ptrn_babies = r'<td>(\w+)</td>'
  ptrn_year = r'Popularity in \b(\d{4})\b'

  babies = np.array(re.findall(ptrn_babies, strFile))
  year = re.findall(ptrn_year, strFile)
    
  babiesMatrix = babies.reshape((-1,3))
    
  babiesRanked = []

  for i in range(np.shape(babiesMatrix)[0]):
      for j in [1,2]:
          strg = " ".join([babiesMatrix[i,j], babiesMatrix[i,0]])
          babiesRanked.append(strg)
    
  babiesSort = np.sort(babiesRanked)
  babiesSort = np.insert(babiesSort, 0, year)
    
  return babiesSort


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

  for file in args:
      output = '\n'.join(extract_names(file)) + '\n'
      f = open("names.html.summary", "a")
      f.write(output+'\n')
      f.close()
      print(output)

  with open('names.html.summary', 'r') as file:
      data = file.read().split('\n\n')
    
  rows = [year.split('\n') for year in data]
  colYears = [rows[i][0] for i in range(len(rows))]
    
  dictn = dict(zip(colYears[:-1], rows))
  namesDf = pd.DataFrame(dictn)
  namesDf = namesDf.drop(0)

  namesDf.to_csv('babyNames')
  
if __name__ == '__main__':
  main()






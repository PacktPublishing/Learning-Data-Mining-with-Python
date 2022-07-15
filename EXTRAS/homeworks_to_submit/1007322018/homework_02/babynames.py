#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


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
  
  a = open(filename,'r') 
  lis = [linea for linea in a]
  lis = " ".join(lis)
  m=re.findall(r"<td>(\d+)</td><td>(\w+)</td>",lis)
  f =re.findall(r"<td>(\d+)</td><td>\w+</td><td>(\w+)</td>",lis)
  
  for i in range(len(m)):
      m[i] = m[i][1] +' '+ m[i][0]

  for j in range(len(f)):
      f[j] = f[j][1] +' '+ f[j][0] 

  d=m+f
  d.sort()
  e = re.findall(r"baby(\d+)",filename)
  d = e+d

  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  return d


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
  
  fileName = args

  if len(fileName) == 1:
    name_list = extract_names(fileName[0])
    text = '\n'.join(name_list) + '\n'
    print(text)
   
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
   
  if len(fileName) > 1:

    for D in fileName:
      name_list = extract_names(D)
      text = '\n'.join(name_list) + '\n'
      files = open(f'{D}.summary','w')
      files.write(text)
      files.close()
    
   
    j=0
    ls = list(range(0,2000))
    df = pd.DataFrame(ls)
    for i in fileName:
      j+=1
      name_list = extract_names(i)

      df.insert(j, name_list[0], name_list[1:], True)
     
    del(df[0])
    df.to_csv('babynames.csv',index=False)
      
      
      



   
  # create Pandas DataFrame with columns being the years and rows being alphabetically listed names 
  # save the frame into CSV file
  
if __name__ == '__main__':
  main()

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


import sys
import re
import io
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
#file= "baby1990.html"

def extract_names(namefile):
    
    file = io.open(namefile).read()

    file_list=file.split("\n")[48:-17]

    año=re.findall(r'(\d{4})',namefile)

    List=[]
    List_sort=[año[0]]

    for i in range (len(file_list)):
        List.append(re.findall(r'<td>(\d+)</td><td>(\b[A-Z]\w+)</td><td>(\b[A-Z]\w+)</td>',file_list[i]))

    for i in List:
        List_sort.append(i[0][1]+i[0][0])
        List_sort.append(i[0][2]+i[0][0])

    List_sort.sort()
    return List_sort


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
    args = sys.argv[1:]
    #print(args)
    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

        
    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    
    
    names_total=[]
    for file in args:
        print(file)
        names_total.append(extract_names(file))
    
        
    if summary == True:

        for año in names_total:
            with open('baby'+str(año[0])+'summary','w') as f: # abrir documento para escribir (write: 'w') como un alias "f" 
                for names in año:
                    f.write(names+'\n') 
                    
                    
    df = pd.DataFrame(names_total).transpose()
    df.to_csv("BabynamesFinal.csv", index= False)
    

      # +++your code here+++
      # For each filename, get the names, then either print the text output
      # or write it to a summary file
      # create Pandas DataFrame with columns being the years and rows being alphabetically listed names 
      # save the frame into CSV file

if __name__ == '__main__':
  main()

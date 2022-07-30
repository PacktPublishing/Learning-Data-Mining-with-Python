#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
#
#By: Joseph Nicolay RA; email: joseph.ruiz@udea.edu.co


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
    
    file=open(str(filename), mode='r').read()
    pattern = '(?i)<h.+>.+ (\d+)</h.+>'
    year = re.findall(pattern, file) #The year of data
    pattern = "(?i)<td>(\d+)</td><td>(\S+)</td><td>(\S+)</td>"
    matches = re.findall(pattern, file) #rank and names for both of them (male and female)
    del file, pattern 
    male_names = [i[1]+' '+i[0] for i in matches]
    female_names = [i[2]+' '+i[0] for i in matches]
    del matches
    names = female_names + male_names
    names.sort()
    del female_names, male_names
    data = year + names
    del year, names 

    return data

def save_file(data,name_File):
    file = open(name_File,'w')   
    for line in data:
        file.writelines(line +'\n')
    return None


def main():
    #Intructions:
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    # create Pandas DataFrame with columns being the years and rows being alphabetically listed names 
    # save the frame into CSV file
    
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)
        
        

    # Notice the summary flag and remove it from args if it is present.    
    summary = False
    DFrame = False 
    
    if args[0] == "--summaryfile":
        summary = True
        del args[0]
        
        for arg in args:
            file = str(arg)
            data = extract_names(file)
            save_file(data,file +".summary")
            print(arg + " is ready")
            
    #Use this flag to make a DataFrame that is saved into CSV File in folder.
    #The commented lines is an alternative way to make it.
    elif args[0] == "--DataFrame":
        DFrame = True
        del args[0]
        
        
        #df_complete = pd.DataFrame({'Names':[]})
        df_complete = pd.DataFrame({})
        for arg in args:            
            data = extract_names(str(arg))
            popularity = {i.split(" ")[0]:i.split(" ")[1] for i in data[1:]}
            dictionary = {'Names': popularity.keys(), data[0]:popularity.values()}
            #df_data = pd.DataFrame(dictionary)
            #df_complete = df_complete.merge(df_data, how='outer', on=df_complete.columns[0], sort=True)
            df_data = pd.DataFrame(popularity.values(), columns=[data[0]], index=popularity.keys())
            df_complete = df_complete.merge(df_data, how='outer', left_index=True, right_index=True)              
          
        print(df_complete.to_string())    
        df_complete.to_csv('Popularity_Names.csv')
    
    #Just print in shell the summary of data per given file in argv[1:0]
    else:        
        for arg in args:
            file = str(arg)
            data = extract_names(file)
            text = '\n'.join(data) + '\n'
            print(text)
  
if __name__ == '__main__':
    main()

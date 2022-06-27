import pandas as pd
import sys
import re


def extract_names(filename): #con regex
    
    import io

    contents = io.open(filename, mode='r',encoding='utf-8').read() #Opens the file 
    lines = contents.split('\n')[48:-17]                           #splits the lines, table is between  lines[48:-17]
    data = re.findall(r'\d{4}',filename)                           #finds the year
    
    for line in lines:
        i = re.findall(r'(\d+)\D+(\b[A-Z]\w+)\D+(\b[A-Z]\w+)',line) #Finds names and rank
        data.append(i[0][1]+' '+i[0][0])                            #rewritting 
        data.append(i[0][2]+' '+i[0][0])
    data.sort()                                                     #reorganizing
    
    return data

"""
#Same function but with pandas 

def extract_names(filename): 
    
    import numpy as np
    
    tables_found = pd.read_html(filename)
    names = tables_found[2][:-1]
    
    names_np = names.to_numpy()
    data =  re.findall(r'\d{4}',filename)
    for i in names_np:
        data.append(i[1]+' '+i[0])
        data.append(i[2]+' '+i[0])
    data.sort()
    return data
"""


def main():
    args = sys.argv[1:]  #Given arguments when running the program
   
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
        
    all_names = []
    for file in args:
        all_names.append(extract_names(file)) 
    
    if summary == True:
        print('Writting summary file(s)...')
  
        for year in all_names:
            f = open(year[0]+'summary', 'w')
            for name in year:
                f.write('%s\n' % name)



  # create Pandas DataFrame with columns being the years and rows being alphabetically listed names 
  # save the frame into CSV file         
    dic = {i[0]: i[1:] for i in all_names}
    df = pd.DataFrame(dic)
    df.to_csv('babynames.csv',index=False) 
            
  
if __name__ == '__main__':
    main()

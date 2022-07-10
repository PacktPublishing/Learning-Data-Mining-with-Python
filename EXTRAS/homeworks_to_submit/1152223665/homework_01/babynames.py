import numpy as np
import pandas as pd
import codecs #Library for open HTML file
import re
import sys



def extract_names(filename):
    #we open the file as string
    file=codecs.open(filename,"r", "utf-8").read()  
    #we use RegEx for find year 
    year=re.findall(r"Popularity in (\d{4})",file)
    #we use RegEx for find names and ranks
    rank_names=re.findall(r"<tr align=\"right\"><td>(\d+)</td><td>(\S+)</td><td>(\S+)</td>",file)
    
    #we save year and rank of names in a list
    Data= []

    Data.append(year[0])
    for i in range(len(rank_names)):
        Data.append(rank_names[i][1]+" "+rank_names[i][0])
        Data.append(rank_names[i][2]+" "+rank_names[i][0])
    
    Data.sort() #we order the list of names alphabetically
    
    return Data
    


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
    
    #we create variables where we saved the columns of data frame and the matrix 
    #with the data called rows
    columns=[]
    rows=[]
    
    #here we fill the previous variables
    for i in args:
        data=extract_names(i)
        columns.append(data[0])
        data.pop(0)
        rows.append(data)
        
    rows=np.array(rows).transpose()
    
    #here we create the data frame and we save the file
    DF=pd.DataFrame(data=rows, columns=columns)
    DF.to_csv("DataFrame_Babynames.csv")
        
    #if the flag summary is true then we save a text file per every html file 
    #with the summary of baby names and his respective rank 
    if summary:
        for i in args:
            f=open(i+".summary.txt", 'w')
            f.write('\n'.join(extract_names(i)) + '\n')
            f.close()
  
if __name__ == '__main__':
    main()
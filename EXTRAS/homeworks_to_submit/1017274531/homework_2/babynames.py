import re
import sys
import codecs
import pandas as pd

#Autor:Nicolás Echeverri Rojas

#Correr como: python babynames.py --print baby1990.html para obtener el punto a)
#Correr como: python babynames.py --sumaryfile baby*.html para obtener el punto b)
#Correr como: python babynames.py --create-DataFrame *.summary para obtener el punto c)
#(se debe de haber creado antes los archivos .summary con las intrucciónes del punto b) para que funcione)

### A,B)
def extract_names(f):
    path=str(f)
    f=codecs.open(path, 'r')
    data=f.read()

    year=re.findall(r"popularity in (\d+)",data, flags=re.IGNORECASE)
    names=re.findall(r"<td>([A-Z]+)</td>",data, flags=re.IGNORECASE)
    numbers=re.findall(r"<td>([0-9]+)</td>",data, flags=re.IGNORECASE)

    girlNames=names[1::2]
    boyNames=names[::2]
    boyNamesNumbers=[boyName+" "+number for boyName,number in zip(boyNames,numbers) ]
    girlNamesNumbers=[girlName+" "+number for girlName,number in zip(girlNames,numbers) ]

    dataYear=year+boyNamesNumbers+girlNamesNumbers
    dataYear.sort(key=lambda x: x[0])
    
    return dataYear


def save_file(data,nameFile):
    file2 = open(nameFile,"w")   
    for element in data:
        file2.writelines(element+'\n')
    return 0


## C)
def create_DataFrame(path):
    f=open(path)
    data=f.read()
    dataList=data.split("\n")
   
    del dataList[-1]  
    dataSplitted= { name.split(" ")[0]:name.split(" ")[1]
               for name in dataList[1:] }
    
    year=dataList[0]
    df=pd.DataFrame( {year:dataSplitted})
    
    return df




def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  
  #el método de sys argv obtiene los argumentos que se pasan por terminal
  #se empieza en el segundo elemento para que no tome el nombre 

  if not args:
    print('usage: [--print] file [file ...] for print in terminal one summary file')
    print('usage: [--summaryfile] file [file ...] for save summary files')
    #Imprime este mensaje si no se suministró argumentos
    print('usage: [--create-DataFrame] file [file ...] to create a DataFrame from the summary files already created')
    sys.exit(1)
  
  # Notice the summary flag and remove it from args if it is present.
 
  summary = False
  if args[0]=='--print':
      del args[0]

      f=str(args[0])
      data=extract_names(f)
      for element in data:
          print(element)

  if args[0] == '--sumaryfile':
    summary = True
    del args[0]
    
    for arg in args:
        f=str(arg)
        data=extract_names(f)
        save_file(data,f+'.summary' )
        print(arg)


  if args[0] == '--create-DataFrame':
    del args[0]
    
    for i in range(len(args)):
        print(args[i])
        if i==0:
            dfMerger=create_DataFrame(args[i])
        else:
            df=create_DataFrame(args[i])
            dfMerger=dfMerger.merge(df,left_index=True, right_index=True, how='outer')

    dfMerger.to_csv("babyNamesAlphabeticalOrder.csv")    

	    
	
	    
  # or write it to a summary file
  # create Pandas DataFrame with columns being the years and rows being alphabetically listed names 
  # save the frame into CSV file




  
if __name__ == '__main__':
  main()

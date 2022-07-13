

import sys  
import re

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
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # Reading the html document
    file = open(f"../../../homeworks_to_download/homework_02/babynames/{filename}", "r")
    
    # Or Reading the html document in the same path, because the *.html also are in this path
    # file = open(f"{filename}", "r")
    
    # Changing the file in a list
    string = " ".join([line for line in file])
    
    # Getting the year of the data
    year = re.findall(r"(\d{4})</h3>|(\d{4})</h2>", string)
    # Getting the year not empty, because for example to file baby2008.html the year is between <h2>...</h2>
    year = [not_empty for not_empty in year[0] if not_empty != '']
    
    # Getting the men and women names and their rankings in tuples
    men_tup = re.findall(r"<td>(\w+)</td><td>(\w+)", string)
    women_tup = re.findall(r"<td>(\w+)</td><td>\w+</td><td>(\w+)</td>", string)
    
    # Converting the tuples in strings on a list
    men = [" ".join(tup[::-1]) for tup in men_tup]
    women = [" ".join(tup[::-1]) for tup in women_tup]
    
    all_names = men + women
    # Sorting alphabetical the list
    all_names.sort()
    
    total_list = year + all_names
    
    return total_list


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
    file = args[0]
    names_list = extract_names(file)
    text = '\n'.join(names_list) + '\n'

    print(text)


def main_part_B():
    
    args = sys.argv[1:]
    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)
    
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # Reading each document .html when somebody use the hint * like *.html to extract all the files ending in .html
    for doc in args:
        file = doc
        names_list = extract_names(file)
        text = '\n'.join(names_list) + '\n'
        # Creating a new file with the summary of ranking names of a baby.html
        new_file = open(f"{doc}.summary", "w")
        new_file.write(text)
        new_file.close()    

  
if __name__ == '__main__':
    
    # Printing the part A of the homework
    # main() 
    
    # Using the part B of the homework, creating the summary files [.summary]
    main_part_B()
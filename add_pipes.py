
# step 1: copy working google sheet to new google sheet, with updated version number (eg. 1.0.1)
# step 2: Copy two columns into new excel spreadsheet. Include all gaps
# step 3: At this time, create new subfolder in version_storage, place excel file in it, with appropriate name
# step 4: Copy excel text, paste into txt document, put that new doc into sentences-five-seven-six, deleting the old one
# step 5: in Python script, type in the correct input file name (the new txt file)
# step 6: delete the current pipes_576.csv file
# step 7: Run the script
# step 8: Place txt file and csv file into today's new version_storage subfolder
# Between runs, there should typically be 3 files at the root folder:  The python script, the latest txt input file, and the latest csv output file.
#     -The txt and csv files should be duplicates of the corresponding files in the latest subfolder of version_storage. 

# NOTICE: each line ends with a RETURN character.  I don't know if that's a good or bad thing, but it affects my indexing in some places.  

# 12-26-2021:  Starting with version_storage>1_0_4  there are 2 extra files:  a json, and a commas_576.csv.  
# -- The json file seems like a smart idea since I use a json file in the mobile app and may use one in various future places.
# -- The commas file is due to no longer using pipes moving into the future.  

# I think after today (12-26-2021) I may no longer have ANY NEED for this python script, since I'll be operating from 
# a csv-type format from the get-go.  That is, my data fields will be in different columns of the google doc, instead of 
# being delineated by the janky { },  # #,  etc.

def add_null_pipe(line: str):
    
    tempList = list(line)
    tempList.insert(line.rindex('|') + 1, 'null|')
    line = ''.join(tempList)

    return line


def add_final_null(line: str):

    if line[-2] == '|':
        line = line[:-1] + 'null' + line[-1:]

    return line    


def add_first_three_pipes(line: str):

    line = line.replace(' ', '|', 1)
    line = line.replace('(', '|', 1)
    line = line.replace(')', '|', 1)

    return line


def add_fourth_pipe(line: str):

     # The [  and ]  characters may appear:  (1) as expected: only at beginning (2) as expected AND later, (3) ONLY later [DON'T NEED TO HANDLE THIS], (4) never

    # for (1) and (2)
    if '| [' in line:

        line = line.replace('| [', '|')
        line = line.replace(']', '|', 1)
    
    # for (4)
    else:

        line = add_null_pipe(line) 

    # random necessary cleanup:
    if '|.' in line:
        line = line.replace('|.', '|')

    return line


def add_fifth_pipe(line: str):

    #remove these unwanted commas from whole document
    line = line.replace('/,', '/ ')


    # The / character may appear:  (1) as paired: /EY-suh/, only at beginning (2) paired at beginning AND unpaired(random) later, 
    # (3) ONLY unpaired(random) later [DON'T NEED TO HANDLE THIS], (4) never

    # scenario (1)
    if '| /' in line:

        first_removed = line.replace('/', '', 1) 
        index_of_second_slash = first_removed.index('/')

        tempList = list(line)
        tempList.insert(index_of_second_slash + 2, '|')
        line = ''.join(tempList)

    else:

        line = add_null_pipe(line)
    
    if '} /' in line:
        print(line)

    return line


# copied from add_fourth_pipe, with a few symbolls changed:
def add_sixth_pipe(line: str):

    if '| <' in line:

        line = line.replace('| <', '|')
        line = line.replace('>', '|', 1)
       
    else:

        line = add_null_pipe(line) 

    # random necessary cleanup:
    if '|.' in line:
        line = line.replace('|.', '|')

    return line


# copied from add_fourth_pipe, with a few symbolls changed:
def add_seventh_pipe(line: str):

    if '| {' in line:

        line = line.replace('| {', '|')
        line = line.replace('}', '|', 1)
       
    else:

        line = add_null_pipe(line) 

    # random necessary cleanup:
    if '|.' in line:
        line = line.replace('|.', '|')

    return line

def add_eighth_pipe(line: str):

    if '| #' in line:
        line = line.replace('| #', '|')
        line = line.replace('#', '|', 1)

    else: 

        line = add_null_pipe(line)

    return line

def remove_spaces_around_pipes(line: str):

    while '| ' in line:
        line = line.replace('| ', '|')
    while ' |' in line:
        line = line.replace(' |', '|')

    return line


def replace_double_quotes_with_single(line: str):

    while '"' in line:
        line = line.replace('"', "'")

    return line
    

def add_pipes(lines: "list[str]"):

    lines2 = []

    for line in lines:

        line = add_first_three_pipes(line)

        line = add_fourth_pipe(line)

        line = add_fifth_pipe(line)

        line = add_sixth_pipe(line)

        line = add_seventh_pipe(line)

        line = add_eighth_pipe(line)

        line = remove_spaces_around_pipes(line)

        line = add_final_null(line)

        line = replace_double_quotes_with_single(line)

        # DO NOT COMMENT OUT:
        lines2.append(line)
    
    return lines2


def format_and_reduce_white_space(lines: "list[str]"):

    for i in range(len(lines)):

        # remove excel tab
        lines[i] = lines[i].replace('\t', ' ')

        # remove extra spaces
        while '  ' in lines[i]:
        
            lines[i] = lines[i].replace('  ', ' ')


    # eliminate rows where pair is a double, like AA and BB.
    # By excluding lines beginning with ' ', we get rid of (1) the rows with "Letter Clarity, no flea" AND (2)the empty rows, which apparently begin with a space (hmm, maybe because i replaced the tab with a space)
    lines2 = []

    for line in lines:

        if line[0] != line[1] and line[0] != ' ':
            
            lines2.append(line)

    return lines2


def examine_syntax(lines: "list[str]"):

    for line in lines:

        # check extra whitespace has been eliminated:
        if '  ' in line:

            print(line[0:2], '  still has extra whitespace:   ', line)
        
    # check if "[" substring exists in line:
    for line in lines:
     
        if '[' not in line:

            print(line[0:2],'  [   not found')
         
    for line in lines:

        if '[' in line:

            if line.index('[') != line.rindex('['):
                print(line[0:2], ' has multiple  [', flush=True)
                print(line)


    for line in lines:

        if '/' in line:
            index = line.index('/')
            print(line[0:2], ' ', index, line[index:index + 30])
        
            result = 0
            for i in line:
                if i == '/':
                    result += 1
            if result > 2:
                print('more than 2: ', result, line[0:2])
        

# to print whole console:  flush=True
with open('sentences-576_12-26-2021_1-0-4.txt') as file:

    lines = file.readlines()

   
    lines = format_and_reduce_white_space(lines)

    # # can comment-out examine_syntax, since it should not alter anything or return anything:
    # # examine_syntax(lines)

    lines = add_pipes(lines)


    for line in lines[500:576]:
        print(line)

with open('pipes_576.csv', 'a', encoding='utf-8') as outputFile:

    outputFile.write('letter_pair|sentence|synopsis|cross_definition|pronunciation|location|tableau|group|backstory\n')

    for line in lines:

        outputFile.write(line)
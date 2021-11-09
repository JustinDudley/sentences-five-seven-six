
# step 1: copy working google sheet to new google sheet, with updated version number (eg. 1.0.1)
# step 2: Copy two columns into new excel spreadsheet. Include all gaps
# step 3: Copy text, paste into txt document
# The repo only has the latest 2 docs, one excel and one txt
# The Daddy should have these two, PLUS a full record of versions for excel and txt
# step 4: Replace the <tab> that follows the pair (ex. AB) with a <space>. I forget how I did this. I should have included that in this script. Oh, maybe i 
#   went back and included it. 
# Now you're ready for this Python script...

# NOTICE: each line ends with a RETURN character.  I don't know if that's a good or bad thing, but it affects my indexing in some places.  

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


def remove_spaces_around_pipes(line: str):

    while '| ' in line:
        line = line.replace('| ', '|')
    while ' |' in line:
        line = line.replace(' |', '|')

    return line
    

def add_pipes(lines: "list[str]"):

    lines2 = []

    for line in lines:

        line = add_first_three_pipes(line)

        line = add_fourth_pipe(line)

        line = add_fifth_pipe(line)

        line = add_sixth_pipe(line)

        line = add_seventh_pipe(line)

        line = remove_spaces_around_pipes(line)

        line = add_final_null(line)

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
with open('sentences-576_11-8-2021_1-0-2.txt') as file:

    lines = file.readlines()

   
    lines = format_and_reduce_white_space(lines)

    # # can comment-out examine_syntax, since it should not alter anything or return anything:
    # # examine_syntax(lines)

    lines = add_pipes(lines)


    for line in lines[500:576]:
        print(line)

with open('pipes_576.csv', 'a', encoding='utf-8') as outputFile:

    outputFile.write('letter-pair|sentence|synopsis|cross-definition|pronunciation|location|tableau|backstory\n')

    for line in lines:

        outputFile.write(line)
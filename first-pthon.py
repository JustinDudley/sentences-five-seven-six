
with open('sentences_576.txt') as file:
    lines = file.readlines()

pipe_lines = []

for line in lines[0:52]:

    line = line.replace(' ', '|', 1)
    line = line.replace('(', '|', 1)

    if '[' in line:

        line = line.replace(')', '|', 1)
        line = line.replace('[', '', 1)
        line = line.replace(']', '|', 1)

    else:

        line = line.replace(')', '||', 1)

    # count the pipes thus far
    count = 0

    for i in line:

        if i == '|':

            count +=1
            
    print(count)

    print(line)

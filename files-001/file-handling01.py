# Creating a file handler to use the txt file
fhand = open('mbox-short.txt')
count = 0
# counting line by line, incrementing the counter at each line
# This way the for loop can read even very large
# file without riskig of running out of memory
# For small files the read() function could be used instead:
# inp = fhand.read()
# print(len(inp))
# (or even print(inp[:20]) to read the first 20 chars of the file
for line in fhand:
    count = count + 1
print('Total of %d lines.' %count)

# Suppose we want to go theough the file line by line
# and only display the lines that start with 'From:' :
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)
# Suppose we don't like the extra blank lines caused 
# by the '\n' character, we can either splice the last
# character of each line or use the strip() method:

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# Or we could use 'if not' and continue

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)



# Handling files in python
#
# Based on the free online book from Prof. Charles Severance (Dr Chuck).
# Requesting a file name, then printing
# some 
# Printing and writing the lines starting with 'Subject:'
# Saving the line up to the rxxxxx reference number.
# protecting the open() with try and except.

filename = input('Enter a file to search: ')
try:
    fhand = open(filename)
except:
    print('Error, file non found.')
    exit()

backupfile = input('What do you want to call the backup? ')
try:
    fhand2 = open(backupfile, 'w')
except:
    print('Error, file non found.')
    exit()

count = 0
upto = 0

for line in fhand:
    if line.startswith('Subject:'):
        upto = line.find(' - ')
        print(line[:upto] + '...')
        fhand2.write(line[:upto] + '\n')
        count = count + 1
print('Found a total of %d subjects.' % count)
fhand2.write('Total of %d entries in this file.\n' % count)
fhand2.close()
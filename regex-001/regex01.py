# PRACTISING WITH REGULAR EXPRESSIONS

import re

myStr = '''
    Destiny shall draw the lightning down from Heaven\n
    Roll its thunder far across  the sea\n
    to where i wait, upon the 'Shore of Wonders'\n
    On the day the sky is open\n
    and the Tree is split asunder.\n
    '''


# match any word of 3 chars followed by a word of 3 to 7 chars with any spaces inbetween
myRE01 = re.compile("\s+(\w{3})\s+(\w{3,7})\s+")

myList01 = re.findall(myRE01, myStr)

# print the 3 char words and the 3 to 7 char words 
for x, y in myList01:
    print('first:{}, second:{}'.format(x, y))

# match any character until the \n, basically getting a line
# the '\n' character is the only character not matched by the '.'
# so there is no nees to add \n after the group ()
myRE02 = re.compile("(.+)")

myList02 = re.findall(myRE02, myStr)

for x in myList02:
    print('line: {}'.format(x))


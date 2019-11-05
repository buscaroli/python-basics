# Learning Python: Strings
# Matteo

import re

s = '''Destiny shall draw the lightning down from Heaven,
Roll its thunder far, across the sea
To where I wait, upon the Shore of Wonders,
On the day the sky is open
And the Tree is split asunder.
Lady Cygna'''

print('Original string:'.center(40, '~'))
print(s)
print('')

split01 = re.split(r'\n', s)
print('''Split string: re.split(r'\n', s):'''.center(40, '~'))
print(split01)
print('')

split02 = re.split(r',.', s)
print("Split string: re.split(r'[,.]', s):".center(40, '~'))
print(split02)
print('')

split03a = s.replace('\n', '')
print('Removed the \\n from the string:')
print(split03a)
print('')
split03b = re.split(r'[,.]', split03a)
print('''Now also split at . and ,:'''.center(40, '~'))
print(split03b)
print('')
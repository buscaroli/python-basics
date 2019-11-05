# PRACTISING REGULAR EXPRESSIONS

import re

myStr = """The quick red fox jumped over
the lazy brown dog"""

# pattern that looks for the word red
re_color = re.compile(r"red")

print(myStr)

# creating a new string where the word identified
# by the pattern (in this case red) is substituted
# with a word passed to the sub function
newStr = re_color.sub("blue", myStr)

print(newStr)

# part 2

myPhoneNumbers = "My old phone number was 07481323, the new ones are 01324567 and 345678"

re_phone_num = re.compile(r"(\d\d+)")

# if the number doesn't start with a 0 is considered invalid
def replacePhoneNum(num):
    # print (num.group(1)) # DEBUGGING LINE
    if num.group(1)[:1] == '0': return '-VALID-'
    else: return '-NOT VALID-'

#print("DEBUG: {}".format(re.findall(re_phone_num, myPhoneNumbers))) #DEBUGGING
print(myPhoneNumbers)

# Validating the phone numbers in an article: re.sub can also
# take a function as an argument: re.sub(regexp, function, string)
myHiddenNumbers = re.sub(re_phone_num, replacePhoneNum, myPhoneNumbers)

print(myHiddenNumbers)
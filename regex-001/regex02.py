# PLAYING AROUND WITH REXULAR EXPRESSIONS

import re

myStr = '''
    This e-mail has been received by bob@gmail.com on the 27/03/2019
    and the subject is "Hi John,\n hope you are well. Those are my
    email addresses: moon@yahoo.co.uk and sun@outlook.it. \nGive me 
    a ring @ 0742-2354124.\nSee you soon\n\nMatt
    '''
# RegEx matching an email:
# [^@\s]+ means: one or more characters that are not @ or a white space
# @ is the @ symbol itself
# [^@\s]+ as above
# [.] is the singol . of the email
# [^@\s.,;:?!]+ is any character apart from punctuation. This last section is
#               used to prevent punctuation at the end of the email address as
#               in sun@outlook.it. (in order to exclude the tailing .) 
re_email = re.compile(r"([^@\s]+@[^@\s]+[.][^@\s.,;:?!]+)")

email_list = re.findall(re_email, myStr)

for email in email_list:
    print("email: {}".format(email))

print("Let's try to use the email pattern to match some emails:")
print("my_email@gmail.ir: {}".format(re_email.match("my_email@gmail.ir")))
print("my_emailATgmail.ir: {}".format(re_email.match("my_emailATgmail.ir")))
print("my_email123@gmail.co.uk: {}".format(re_email.match("my_email123@gmail.co.uk")))

# Finding a list of words using the boundary character \b
re_word = re.compile(r"\b(\w+)\b")

word_list = re.findall(re_word, myStr)

for word in word_list:
    print("word: {}".format(word))

# Finding all numbers that could be dates, phone numbers
# or simple numbers
# \b is a boundary (like a space...)
# \d+ means one or more digits
# [-/\s]? means zero or one of the symbols included within the []
# [\d]* means zero or more digits
# [-/\s]? same as above
# [\d]* means zero or more digits
# \b is a boundary
re_number = re.compile(r"\b(\d+[-/\s]?[\d]*[-/\s]?[\d]*)\b")

number_list = re.findall(re_number, myStr)

for num in number_list:
    print("number: {}".format(num))


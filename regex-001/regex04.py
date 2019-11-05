
# PRACTISING REGULAR EXPRESSIONS
# BACKREFERENCING

import re

myStr = """01/06/2018 200
02/06/2018 212
03/06/2018 175
04/06/2018 245
07/06/2018 212
Extra of 100 BONUS
08-06-18 200
09-06-18 212"""

# Matching UK dates (dd/mm/yyyy or dd-mm-yy), identifying four groups 
# that will be use for Backreferencing
re_UK_dates = re.compile(r"\b(\d\d)([-/])(\d\d)[-/](\d{2,4})\b")

# Converting UK dates (dd/mm/yyyy) into US dates (mm/dd/yyyy) keeping the same
# separator ( / or -)
# \1 is the day
# \2 is the symbol used as a separator (/ or -)
# \3 is the month
# \4 is the year
# switched from \1 \2 \3 \2 \4 to \3 \2 \1 \2 \4 
US_dates = re_UK_dates.sub(r"\3\2\1\2\4",myStr)
print("Original string with UK dates:\n{}".format(myStr))
print("Modified string with US dates:\n{}".format(US_dates))


###### NAMED  GROUPS ########

# Let's do it all aagain using named groups
# The groups have been given a name, in this case day month year and sep 
# and it's easier to know what's going on by looking at the regular
# expression pattern
re_UK_dates_named_groups = re.compile(r"\b(?P<day>\d\d)(?P<sep>[-/])(?P<month>\d\d)[-/](?P<year>\d{2,4})\b")
US_dates_named_groups = re_UK_dates_named_groups.sub(r"\g<month>\g<sep>\g<day>\g<sep>\g<year>",myStr)

print("Modified string using Named Groups:\n{}".format(US_dates_named_groups))
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

a = datetime(2019, 10, 8)
print('8th of October 2019, default: {}'.format(a))

b = timedelta(days=7)
c = a+b
print('Adding a timedelta of 7 days: {}'.format(c))

now = datetime.today()
print('Current time: {}'.format(now))

time_italy = timedelta(hours=1)
print('Current time in Italy (if living in the UK): {}'.format(now+time_italy))

my_date = datetime(1825, 4, 1)
print(my_date)
following_week = my_date + timedelta(weeks=1)
following_week_improved = following_week.strftime('%A %d %B %Y')
print('The following week would have been the {}'.format(following_week_improved))
print(my_date.strftime("%A %d %B %Y"))

years_passed = (int(now.strftime('%Y')) - int(my_date.strftime('%Y')))
print('It has been {} years since the 1st April 1825'.format(years_passed))


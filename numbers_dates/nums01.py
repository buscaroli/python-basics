# Learning Python
# Matteo

x = input('Enter a number:')
print(x)
if not '.' in x:
    print('Sum of Ints: {}'.format(5 + int(x)))
elif '.' in x:
    print('Sum of floats: {}'.format(5.0 + float(x)))

print(round(545.034123,-1))

num = int(input('Enter an integer:'))
sum = int(0)
for i in range(num+1):
    sum +=  i**3
print('The sum of the cubes of the first {} nums is {}'.format(num, sum))

mult = 1
while True:
    n = input('Enter a number or press enter to quit:')
    if n == '':
        break
    mult *= int(n)  
print('The value of the numbers multiplied is {}'.format(mult))

#Getting the day, month and year from a given date
[day, month, year] = (input('Enter the date dd/mm/yyyy:')).split('/')
print('Day: {}, Month: {}, Year: {}'.format(day, month, year))

for x in [day, month, year]:
    print (x)

def convert_day(d):
    if (d == '01'):
        return('1st')
    elif (d == '02'):
        return('2nd')
    elif (d == '03'):
        return('3rd')
    elif (d == '31'):
        return('31st')
    else:
        return(d + 'th')

for x in [convert_day(day), month, year]:
    print(x)

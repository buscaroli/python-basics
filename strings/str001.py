# LEARNING PYTHON3
# Starting with a dictionary of 3 elements, ask the user for a name
# if name in dictionary print name and address (key-value pair)
# if not ask for the address and add it to the dictionary
# Matteo

addresses = {'Matt': 'Commercial Rd', 'Mel': 'Oxford St', 'Eric': 'High St'}

while True:
    print('Enter a name, or press enter to quit')
    name = str(input())
    if name == '':
        break 

    if name in addresses.keys():
        print('{} lives at {}'.format(name, addresses[name]))
    else:
        print('{} is not in my list'.format(name))
        print('Where do they live?')
        addr = str(input())
        addresses[name] = addr

    for v, k in addresses.items():
        print('{} lives at {}'.format(v, k))
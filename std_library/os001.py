import os

print(f'''Your operating system type is {os.name}''')
print(f'''Extra info: {os.uname()}''')
print(f'''Home: {os.environ['HOME']}''')
print(f'''Shell: {os.environ['SHELL']}''')
# CHANGING DIRECTORY
print(f'Current directory: {os.getcwd()}')
usr_dir = '/usr/'
print('Going to /usr:')
os.chdir(usr_dir)
curr_dir = os.getcwd()
print(f'Current directory: {os.getcwd()}')
print(f'You are logged in as {os.getlogin()}')


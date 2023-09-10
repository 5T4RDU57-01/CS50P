'''
1- take input in camel case

2- add an underscore before the capitalized word

3- return it in lowercase
'''

camel_case = input('Enter your name in camel case: ')
for c in camel_case:
    if c.islower():
        print(c, end='')
    if c.isupper():
        print(f'_{c.lower()}', sep='',end='')
    
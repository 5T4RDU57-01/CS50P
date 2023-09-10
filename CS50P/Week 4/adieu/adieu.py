'''
mylist = p.join(("apple", "banana", "carrot"))
# "apple, banana, and carrot"
'''
import inflect
p = inflect.engine()


goodbye = 'Adieu, adieu, to'
name_list = []

while True:
    try:
        name = input('Name: ').title()
        name_list.append(name)
    except EOFError:
        print(f'\n{goodbye} {p.join(name_list)}')
        break

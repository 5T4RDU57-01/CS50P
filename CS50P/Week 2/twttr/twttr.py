'''
Tkes input and removes all vovels from the text

'''
vovels = ['A', 'a', 'E', 'e', 'I', 'i' , 'O', 'o' ,'u' , 'U']

def main():
    text = input('Input: ')
    print(f'Output: {remove_vovels(text)}')

def remove_vovels(string):
    for s in string:
        if s in vovels:
            string = string.replace(s, '')
        else:
            pass
    return string

main()
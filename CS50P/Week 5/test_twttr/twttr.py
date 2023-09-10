def main():
    text = input('Input: ')
    print(f'Output: {shorten(text)}')



def shorten(word):
    vovels = ['A', 'a', 'E', 'e', 'I', 'i' , 'O', 'o' ,'u' , 'U']

    for s in word:
        if s in vovels:
            word = word.replace(s, '')
        else:
            pass
    return word



if __name__ == "__main__":
    main()
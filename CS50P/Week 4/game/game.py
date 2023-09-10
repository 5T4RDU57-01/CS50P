import random
import sys

def main():
    n = get_n()
    guess_no = random.randint(1 , n)
    while True:
        try:
            guess = int(input('Guess: '))
            if guess == guess_no:
                print('Just right!')
                break

            elif guess > guess_no:
                print('Too large!')
                pass
            else:
                print('Too small!')
                pass
        except:
            pass
    sys.exit()




def get_n():
    while True:

        n = input('Level: ')
        if n.isnumeric():
            if int(n) < 1:
                continue
            else:
                return int(n)
        else:
            continue

main()
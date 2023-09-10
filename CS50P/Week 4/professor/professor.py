import random


def main():
    score = 0
    level = get_level()

    for i in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        correct_answer = a + b
        tries = 3
        while True:

            if tries == 0:
                print(f'{str(a)} + {str(b)} = {str(correct_answer)}')
                tries -= 1
                break

            answer = int(input(f'{str(a)} + {str(b)} = '))

            if answer == correct_answer:
                score += 1
                break

            else:

                print('EEE')
                tries -= 1
                continue



    print(f'Score: {score}')





def get_level():
    while True:
        level = (input('Level: '))
        if level == '1' or level == '2' or level == '3':
            return level
        else:
            continue


def generate_integer(level):
    int = 0
    try:
        if level == '1':
            int = random.randint(0 , 9)
        elif level == '2':
            int = random.randint(10 , 99)
        elif level == '3':
            int = random.randint(100 , 999)
        else:
            raise ValueError

        return int
    except ValueError:
        get_level()






if __name__ == "__main__":
    main()
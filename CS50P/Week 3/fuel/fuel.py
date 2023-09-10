def main():
    percentage = fuel()

    if percentage >= 99:
        print('F')
    elif percentage <= 1:
        print('E')
    else:
        print(f'{percentage}%')



def fuel():
    while True:
        try:
            fraction = (input('Fraction: '))
            x , y = fraction.split('/')
            x , y = int(x) , int(y)

            if x > y:
                continue
            else:

                percentage = round(((x / y) * 100))

                return percentage

        except ValueError:
            pass

        except ZeroDivisionError:
            pass


main()
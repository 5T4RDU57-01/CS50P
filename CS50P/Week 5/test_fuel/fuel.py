def main():
    fraction = (input('Fraction: '))
    percentage = convert(fraction)
    print(gauge(percentage))


# retruns percentage
def convert(fraction):
    try:
        x , y = fraction.split('/')
    except:
        raise ValueError
    if x.isdigit() == False or y.isdigit() == False:
        raise ValueError
    if y == '0':
        raise ZeroDivisionError
    x , y = int(x) , int(y)

    if x > y:
        raise ValueError
    else:

        percentage = round(((x / y) * 100))

        return percentage






# returns E, F or {percentage}%
def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
import validators

def main():
    print(validation(input('E-mail: ')))


def validation(email):
    if validators.email(email):
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == '__main__':
    main()
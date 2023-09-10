def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    validity = True

    n = 0

    if(len(s) < 2 or len(s) > 6 ):
        validity = False
        return  validity

    if(s[0].isdigit() or s[1].isdigit()):
        validity = False
        return  validity
    for c in s:

        if( not c.isalnum()):
            validity = False
            return  validity

        if(n > 1 and c.isalpha()):
            validity = False
            return  validity

        if(c.isdigit()):
            n += 1

        if(n == 1 and c == "0"):
            validity = False
            return  validity

    return  validity




if __name__ == '__main__':
    main()
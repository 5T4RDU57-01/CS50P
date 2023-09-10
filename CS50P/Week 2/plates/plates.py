'''
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. must not start with 0”
“No periods, spaces, or punctuation marks are allowed.”

'''


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




main()
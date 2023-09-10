import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


# must be a number between 0-255
def validate(ip):
    validity = True
    if re.search(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$' , ip):
        pass
    else:
        validity = False
        return validity

    numbers = ip.split('.')

    for num in numbers:
        if 0 <= int(num) <= 255:
            pass
        else:
            validity = False
            return validity

    return validity






if __name__ == "__main__":
    main()
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')

    number = get_lines(sys.argv[1])
    print(number)


def get_lines(filename):
    if filename.endswith('.py') == False:
        sys.exit('Not a Python file')

    count = 0
    try:
        with open(filename , 'r') as file:
            for line in file:
                if (line.lstrip()).startswith('#'):
                    pass
                elif line.strip() == '':
                    pass
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit('File does not exist')

    return count


if __name__ == '__main__':
    main()
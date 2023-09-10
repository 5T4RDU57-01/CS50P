from tabulate import tabulate
import sys
import csv



def main():
    if len(sys.argv) == 1:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if sys.argv[1].endswith('.csv') == False:
        sys.exit('Not a csv file')

    print(tabulate(format_data(sys.argv[1]),headers=header(sys.argv[1]), tablefmt="grid"))


def format_data(data):
    table = []
    count = 0
    try:
        with open(data) as file:
            csvreader = csv.reader(file)
            for line in csvreader:
                if count == 0:
                    count += 1

                else:
                    table.append(line)
                    count += 1
    except FileNotFoundError:
        sys.exit('File does not exist')

    return table

def header(filename):
    count = 0
    header = 0
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for line in reader:
                if count == 0:
                    header = line
                    return header
                else:
                    count += 1
                    pass
    except FileNotFoundError:
         sys.exit('File does not exist')


if __name__ == '__main__':
    main()

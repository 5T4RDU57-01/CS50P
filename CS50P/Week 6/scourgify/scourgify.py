'''

Take input of two filenames (reading and writing)
arrange contents from [name, house] to [firstname , lastname , house]
write that to a new file

'''
import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    list_dictionary = arrange(sys.argv[1])
    write_to_file(list_dictionary)



def arrange(readfile):
    new_ldict = []
    try:
        with open(readfile) as r:
            reader = csv.DictReader(r)
            for line in reader:
                names = line['name'].split(',')
                new_ldict.append({'first' : names[1] , 'last' : names[0] , 'house' : line['house']})
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

    return new_ldict


def write_to_file(ldict):
    with open(sys.argv[2] , 'w') as writefile:
        writer = csv.DictWriter(writefile , fieldnames=['first' , 'last' , 'house'])
        writer.writeheader()
        i = 0
        for _ in ldict:
            writer.writerow({'first' : ldict[i]['first'].lstrip() ,
                              'last' : ldict[i]['last'] ,
                                'house' : ldict[i]['house']})
            i += 1



if __name__ == '__main__':
    main()

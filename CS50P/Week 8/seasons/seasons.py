import datetime
import sys
import inflect
import re



def main():
    date_of_birth = input('Date of birth: ')

    if validation(date_of_birth) == False:
        sys.exit('Invalid date')


    mins = get_minutes(date_of_birth)

    print(f'{mins_to_words(mins)} minutes')


def validation(dob):
    match = re.match(r'(?:[1-2][0-9]{3})-(?:([0-1][0-2]|[0][1-9]))-(([0-2][0-9]|[3][0-1]))' , dob)
    if match:
        if int(match.group(1)) == 0:
            return False
        else:
            return True
    else:
        return False

def get_minutes(dob):
    today = str(datetime.date.today())

    year , month , day = today.split('-')
    date_one = datetime.datetime(int(year) , int(month) , int(day))

    year2 , month2 , day2 = dob.split('-')
    date_two = datetime.datetime(int(year2) , int(month2) , int(day2))

    return round(((date_one - date_two).total_seconds()) / 60)


def mins_to_words(mins):
    p = inflect.engine()
    words = p.number_to_words(mins ,andword='').capitalize()
    return words






if __name__ == "__main__":
    main()
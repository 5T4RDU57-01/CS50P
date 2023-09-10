months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = get_date()
    print(date)



def get_date():
    while True:
        date = input('Date: ')
        try:
            if '/' in date:
                month , day , year = map(int, date.split('/'))
            else:
                month , day , year = date.split(' ')
                if ',' in day:
                    day = day.replace(',' , '')
                else:
                    continue
                month = (months.index(month)) + 1

            if (0 < int(month) <= 12) and (0 < int(day) <= 31):
                if int(month) < 10:
                    month = f'0{month}'
                else:
                    pass
                if int(day) < 10:
                    day = f'0{day}'
                else:
                    pass
                format_date = f'{year}-{month}-{day}'
                return format_date

            else:
                continue
        except ValueError:
            continue

main()
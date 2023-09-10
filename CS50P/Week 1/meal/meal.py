#  Breakfast from 8-9 lunch from 12-13 dinner from 18-19
def main():
    user_time = input("What's the time? ")

    if (user_time.lower())endswith('a.m') or (user_time.lower())endswith('p.m'):
        twelve_hour(user_time)
    else:
        return

    if 7.0 <= convert(user_time) <= 8.0:
        print("breakfast time")
    elif 12 <= convert(user_time) <= 13:
        print('lunch time')
    elif 18 <= convert(user_time) <= 19:
        print('dinner time')
    else:
        print()


# converts time to 24 hour format (7:30 to 7.5)
def convert(time):
    x , y = time.split(':')
    mins = int(y) / 60
    act_time = int(x) + mins
    return act_time


if __name__ == "__main__":
    main()
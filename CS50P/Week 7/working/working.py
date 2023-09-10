import re



def main():
    print(convert(input("Hours: ")))


# take as input time in 12 hour format and then convert it to 24 hour format
def convert(time):
    exp = (r'(0?[1-9][0-2]?):?([0-5][0-9])? (AM|PM)')
    match = re.search(r'^' + exp + ' to ' + exp + '$' , time)
    if match:
        time_one = twenty_four(match.group(1) , match.group(2) , match.group(3))
        time_two = twenty_four(match.group(4) , match.group(5) , match.group(6))
        return f'{time_one} to {time_two}'
    else:
        raise ValueError



def twenty_four(hours , mins , m):
    if hours == "12":
        if m == "AM":
            hours = "00"
        else:
            hours = "12"
    else:
        if m == "AM":
            hours = f"{int(hours):02}"
        else:
            hours = f"{int(hours)+12}"
    if mins == None:
        mins = "00"
    else:
        mins = f"{int(mins):02}"
    return f"{hours}:{mins}"







if __name__ == "__main__":
    main()
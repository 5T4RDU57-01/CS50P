shopping_list = {}

while True:
    try:
        item = input().upper()
        if item in shopping_list:
            shopping_list[item] += 1
        else:
            shopping_list[item] = 1
    except KeyError:
        pass
    except EOFError:
        break

sorted = []

for thing in shopping_list:
    sorted.append(thing)

sorted.sort()

for key in sorted:
    print(f'{shopping_list[key]} {key}')
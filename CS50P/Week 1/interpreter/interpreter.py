expression = input('Enter your expression: ').strip()

x , y , z = expression.split(' ')
x , z = float(x) , float(z)

def calculate(a , b, c):
    if b == '+':
        result = a + c
    elif b == '-':
        result = a - c
    elif b == '*':
        result = a * c
    elif b == '/':
        result = a / c
    else:
        print('Invalid Operator.')
    print(result)

calculate(x , y , z)
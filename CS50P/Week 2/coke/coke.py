'''
prompts for input using while loop
total decremented until it reches < 0
breaks out of while loop and outputs amount due
amount accepted =  25 , 10 , 5
'''
total = 50
denominations = [25 , 10 , 5]
paid = 0

while paid < 50:
    print(f'Amount Due: {total - paid}')
    insert = int(input('Insert Coin: '))
    if insert not in denominations:
        continue
    else:
        paid = paid + insert

print(f'Change Owed: {paid - total}')


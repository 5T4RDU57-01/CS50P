import sys
import requests

if len(sys.argv) == 1:
    sys.exit('Missing command-line argument')
if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
try:
    sys.argv[1] = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')
try:
    data = (requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')).json()
    price = float((((data['bpi'])['USD'])['rate']).replace(',' , '')) * float(sys.argv[1])

    print(f'${price:,.4f}')
except requests.RequestException:
    print('An unexpexted error occured, try again later')
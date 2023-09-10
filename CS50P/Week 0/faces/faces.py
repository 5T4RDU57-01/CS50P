def main():
    converted = convert(input('Enter your text: '))
    print(converted)

def convert(text):
    return text.replace(':(', '🙁').replace(':)', '🙂')

main() 
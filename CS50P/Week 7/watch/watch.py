import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(html):
    try:
        if link := re.search(r'http(?:s)?://(?:www\.)?youtube\.com/embed/(.+)"' , html).group(1):
            return f'https://youtu.be/{link}'
        else:
            return None
    except AttributeError:
        return None









if __name__ == "__main__":
    main()
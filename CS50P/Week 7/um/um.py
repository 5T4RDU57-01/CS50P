import re



def main():
    print(count(input("Text: ")))


def count(s):
    s = f' {str(s).lower()} '
    count = len(re.findall(r'[~!@#$%^&*\(\)_+-=\:\";\?\.,<>/ ]um[~!@#$%^&*\(\)_+-=\:\";\?\.,<>/ ]', s))
    return count





if __name__ == "__main__":
    main()
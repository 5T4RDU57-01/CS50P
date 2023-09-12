from  cryptography.fernet import Fernet
from tabulate import tabulate
import sys


def main():
    if len(sys.argv) == 1:
        user_intefrace()
    elif len(sys.argv) < 5:
        command_line_intefrace()
    else:
        print('Invalid usage, use "-h" command to display help menu.')


def user_intefrace():
    while True:
        try:
            make_table()
            choice = input('Select a process: ')
            if ui_validation(choice) == False:
                print('\nPlease select from one of the options or input "3" for help menu.')
                continue

            choice = int(choice)

            if choice == 0:
                file = input(r'Enter file name: ')
                key = input(r'Enter key name: ')
                if key_validation(key) == False:
                    print('Key must end in ".key"')
                    continue
                if encrypt(file , key) == False:
                    print('\nFile and/or key does not exist. Please re-check your input.')
                    continue
                

            elif choice == 1:
                file = input(r'Enter file name: ')
                key = input(r'Enter key name: ')
                if key_validation(key) == False:
                    print('Key must end in ".key"')
                    continue

                if decrypt(file , key) == False:
                    print('\nFile and/or key does not exist. Please re-check your input.')
                    continue
                
            elif choice == 2:
                key = input(r'Enter key name: ')
                if key_validation(key) == False:
                    print('Key must end in ".key"')
                    continue
                if generate_key(key) == False:
                    print('\nNo Such file or directory, please try again.')
                    continue

            elif choice == 3:
                help()
                break
                

            elif choice == 4:
                sys.exit('\nThank you for using the program!\nExiting now...')

        except EOFError:
            sys.exit('\nThank you for using the program!\nExiting now...')
        

def ui_validation(usr_input):
    try:    
        usr_input = int(usr_input)
    except:
        return False
    if not (0 <= usr_input <= 4):
        return False
    
    return True


def make_table():
    intefrace = [['Index' , 'Process' , 'Description'] , 
                 ['[0]' , 'Encryption' , 'Encrypt a file'],
                 ['[1]' , 'Decryption' , 'Decrypt a file'],
                 ['[2]' , 'Key generation' , 'Generate a symmetric key'],
                 ['[3]' , 'Help' , 'Display the Help menu'],
                 ['[4]' , 'Exit' , 'Exit the program'],
                 ]
    

    print(f"\n{tabulate(intefrace , headers='firstrow' , tablefmt='outline')}\n{('_' * 55).strip()}\n" )


def command_line_intefrace():
    try:
        if cli_validation(fr'{sys.argv[1]}' , len(sys.argv) , fr'{sys.argv[3]}') == False:
            sys.exit('\nInvalid usage. Use "-h" for help menu\n')
    except IndexError:
        if cli_validation(fr'{sys.argv[1]}' , len(sys.argv), sys.argv[2]) == False:
            sys.exit('\nInvalid usage. Use "-h" for help menu\n')

    if sys.argv[1] == '-e':
        if encrypt(fr'{sys.argv[2]}' , fr'{sys.argv[3]}') == False:
            print('\nFile and/or key does not exist. Please re-check your input.\n')
    elif sys.argv[1] == '-d':
        if decrypt(fr'{sys.argv[2]}' , fr'{sys.argv[3]}') == False:
            print('\nFile and/or key does not exist. Please re-check your input.\n')
    elif sys.argv[1] == '-g':
        if generate_key(fr'{sys.argv[2]}') == False:
            print('\nNo such file or directory, please try again.\n')
    elif sys.argv[1] == '-h':
        help()
    

def cli_validation(process , length , key):
    if length == 4:
        if process == '-e' or process == '-d':
            return key_validation(key)
        else:
            return False
    elif length == 3:
        if process == '-g':
            return key_validation(key)
        else:
            return False
        
    elif length == 2:
        if not process == '-h':
            return False
        
    else:
        return False
    
    return True
    

def encrypt(filename , key):

    try:
        with open(key , 'rb') as fkey:
            key = fkey.read()
        fer = Fernet(key)
        with open(filename , 'rb') as file:
            plaintext = file.read()
        ciphertext = fer.encrypt(plaintext)
        with open(filename , 'wb') as write_file:
            write_file.write(ciphertext)

    except FileNotFoundError:
        return False
    
    print('File encrypted.\n')
    

def decrypt(filename , key):

    try:
        with open(key , 'rb') as fkey:
            key = fkey.read()
        fer = Fernet(key)
        with open(filename , 'rb') as file:
            ciphertext = file.read()
        plaintext = fer.decrypt(ciphertext)
        with open(filename , 'wb') as write_file:
            write_file.write(plaintext)

    except FileNotFoundError:
        return False
    
    print('File decrypted.\n')


def generate_key(name):
    key = Fernet.generate_key()
    try:
        with open(name , 'wb') as file:
            file.write(key)
    except FileNotFoundError:
        return False

    print('Key has been generated.\n')


def key_validation(key):

    key = str(key)

    if key.endswith('.key') == False:
        return False
    return True


def help():
    
    printing = [
    f"\n{'_' * 55}\n"
    '\nCOMMAND LINE USAGE:'
    '\n<Python project.py –e / -d / -g <File name> <Key Name>?>\n'
    '\n\n-e	Encrypt a specified file with specified key'
    '\n-d	Decrypt a specified file with specified key'
    '\n-g	Generate a symmetric key with the specified name'
    '\n-h	Display the help menu\n'
    '\nUI USAGE:\n'
    '\n<Python project.py>\n'
    '\nInput the following:\n'
    '\n“0”	To encrypt a file'
    '\n“1”	To decrypt a file'
    '\n“2”	To generate a symmetric encryption key'
    '\n“3”	To display the help menu'
    '\n“4”	To exit the program\n'
    f"{'_' * 55}\n"

    ]

    for item in printing:
        print(item)


if __name__ == '__main__':
    main()
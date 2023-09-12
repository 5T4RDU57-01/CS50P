# EVENT HORIZON
#### Video Demo:  https://youtu.be/hkr8o5VLtPI
#### Description:
    
### project.py:

    This is a program that encrypts and decrypts files using symmetric encryption from the Cryptography library of Python.
    Moreover, it generates symmetric encryption keys.

## main:

    This fucntion first checks the amount of command-line arguments given by the user. If no command-line arguments are given,
    it calls the "user_interface" function that displays the interface which can be used by the user to select the process they want to perform. 

    If less than five command-line arguments are given, it calls the "command_line_interface" function that performs a process based on the 
    command-line arguments given by the user. Lastly, if five or more command-line arguments are given, it tells the user to use the
    "-h" command from the command line to display the help menu.

## encrypt:

    This function takes as input the name of the file to be encrypted and the key to encrypt it with. First, it opens and
    reads the file containing the key and stores it in a variable called "key" and then passes it to the "Fernet" class. Then, it opens the file to be
    encrypted and encrypts it using the given key. 
    
    If either the file to be encrypted or the key are not found, the function returns the boolean value"False" (used to display error messages
    in other functions). Otherwise, the user is informed that the file has been encrypted.

## decrypt:

    This function, like the "encrypt" function, takes as input the name of the file to be decrypted and the key to decrypt it with.
    The file containing the key is opened, read and stored in a variable called "key" and passed to the fernet class. Then, the file to be decrypted
    is opened and read. The ciphertext in the file is then decrypted using the given key and written back to the file, replacing the ciphertext.

    If the key or the file to be decrypted is not found, the function returns the boolean value "False" (used to display error messages in other fuctions)
    If everything goes smoothly, The user is informed that the file has been decrypted.

## generate_key:

    This function takes as input the name of the key to be generated and generates a symmetric encrption/decryption key with the same name.
    If the user specifies a directory to save the key in and the directory does not exist, the function returns the boolean value "False" (used to display error
    messages in other functions). If key generation is successful, the user is informed that the key has been generated.

## key_validation:

    This function is used to validate if a user has entered a key in the correct format. The name of the key is first converted into a string and then 
    it is checked that the key is in the ".key" format. If it is not, the functions returns the boolean value "False".

## help:

    This function prints the help menu which displays the usage of the program and what process each of the commands correspond to.

## command_line_interface:

    This fucntion uses the given-command line arguments to perform a specific process. It first calls the "cli_validation" function and
    tries to give it as input the process command, the length of command-line arguments and the key. If nothing is at the third index of the
    command-line arguments is it still calls the"cli_validation" function  but this time, gives it as input the process, length of command-line
    arguments and the key(which is now at the second index of command-line arguments, this can happen of the user wants to generate key). 

    Then, depending on the first command-line argument, it performs a specific process ("-e" for encryption, "-d" for decryption, "-g" to generate
    a key and "-h" to display help menu). However if the return value of any of the functions for the processes is false, an error message is displayed.

## cli_validation:

    This function validates that the user has used the command-line arguments correctly. It takes as input the process, number of command-line
    arguments and the name of the key. if the number of the command line arguments is four, and the process is either "-e" or "-g", it checks and returns 
    the validity of the key using the "key_validation" function. If the process are not '-e" or "-d", the function returns the boolean value "False". 

    If the number of command ine arguments if three and the process is not "-g", the function returns the boolean value "False", otherwise, 
    it checks and returns the validity of the key using the "key_validation" function. 
 
    if the number of command-line arguments is two and the process is not "-h", the function returns the boolean value "False".

## user_interface:

    The "user_interface" funtion starts off by making a table displaying the inputs the user can give, the processes they correspond to and
    a brief description of the processes (using the make_table function). The user is then prompted for a input and depending on this input, a process
    is performed. The user is prompted until they perform the exit process or send an EOF signal. The "ui_validation" function validates if the user has
    inputted the correct index of a process.

    If "0" (encryption) is inputted, the user is prompted for the name of the file they want to encrypt and the key that the want to encrypt it with. 
    If the key is not in the correct format or if the file to be encrypted does not exist, an error message is displayed and the user is prompted again.   

    If "1" (decryption) is inputted, the user is prompted for the name of the file they want to decrypt and they key they want to decrypt it with.
    if they key is not in the correct format or if the file to be decrypted does not exist, an error message is displayed and the user is prompted again.

    If "2" (key generation) is inputted, the user is prompted for the name of the key they want to create. The format if the key is checked using the 
    "key_validation" function and if the function's return value is "False", an error message is displayed.

    If "3" (help) is inputted, the help menu is displayed and the program exits.

    Lastly, if "4" (exit) is inputted or an EOF signal is given, the program displays a "Thank you" message and exits. 

## ui_validation:

    This function validates the user's input. If the input is not a number or if it is not between 0 and 4 inclusive, the function returns the boolean
    value "False". Otherwise, it returns the bolean value "True".

## make_table:

    This function makes a table displaying the inputs the user can give, the processes they correspond to and a brief description of the processes.


### Related files and directories:

## requirements.txt:

    This files coontains the pip-installable modules required to run the program.

## test_project.py:

    This file contains the tests used on the program using pytest. Every function that returns a value was tested.

## key_file:

    This directory contains two files; "existant-file.txt" and "existant-key.key". These files were used in the testing of the program to validate
    that the program caught the inputted files that did not exist and ran smoothly if they did, infact, exist.

## README.md:

    This is the file you are reading right now. If you did read all of this, thank you. CS50P has been an amazing and highly educational experiance for
    me and probably most of the students that took it. I look forward to taking a few more CS courses.
    P.S, David Malan was awesome. <3

    byeee :33 
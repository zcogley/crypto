from sys import argv, exit
from helpers import alphabet_position, rotate_character

def user_input_is_valid(cl_args):
    if len(cl_args) != 2:
        print("usage: python3 caesar.py n")
        return False 
    if cl_args[1].isdigit() == False:
        print("usage: python3 caesar.py n")
        return False
    return True

def encrypt(text, rot):
    rtr_str = ''
    for char in text:
        rtr_str = rtr_str + rotate_character(char, rot)

    return rtr_str

def main():
    if user_input_is_valid(argv) == False:
        exit()
    print(encrypt(input("Type a message:\n"), int(argv[1])))

if __name__ == '__main__':
    main()

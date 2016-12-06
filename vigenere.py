from helpers import alphabet_position, rotate_character
import string

def encrypt(text, str):
    test_str = string.ascii_lowercase
    test_str2 = string.ascii_uppercase

    rtr_str = ''
    rot_lst = []
    rot_val = 0
    i = 0

    str2 = str.lower()

    for chr in str2:
        rot_lst.append(test_str.find(chr))

    for char in text:
        rot_val = rot_lst[i]
        rtr_str = rtr_str + rotate_character(char, rot_val)

        if char.isalpha() == True:
            i += 1
            i = i % len(str)


    return rtr_str

def main():
    print(encrypt(input("Type a message:\n"), (input("Rotate by:\n"))))

if __name__ == '__main__':
    main()

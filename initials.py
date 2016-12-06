def get_initials(fullname):
    """Given a person's name, return the person's initials (uppercase)"""

    parts = fullname.split()
    new_str = ''
    for name in parts:
        new_str = new_str + name[0]
        rtr_str = new_str.upper()
    return rtr_str

def main():
    get_initials(fullname = input("What is your full name?\n"))

if __name__ == '__main__':
    main()


#!/usr/bin/python
from sys import argv,exit
from helpers import alphabet_position, rotate_character

def encrypt(string,rot):
    cryption = ''
    for i in string:
        cryption = cryption+ rotate_character(i,rot)
    return cryption

# def user_input_is_valid(cl_args):
#     #cl_args = int(cl_args)
#     if len(cl_args) != 2:
#         return False
#
#     if cl_args[1].isdigit():
#         return True
#     else:
#         return False
def user_input_is_valid(cl_args):
    test = cl_args.index()
    print(test)
    if len(cl_args) == 1 and test.isdigit():
        return True
    else:
        return False
def main():
    if user_input_is_valid(argv):
        rot = int(argv[1])
        text = input("Type some text:")
        print(encrypt(text,rot))
    else:
        print("usage: python3 caesar.py n")
        exit()

if __name__ == '__main__':
  main()

# This program takes in a user input when running the program as an argument
# that number is a key that will shift the associated text that the user enters
# next and shifts every letter that amount
import sys

def main(argv):
    try:
        sys.argv[1] == None
    except IndexError:
        print("Usage: python " + sys.argv[0] + " k")
        return 0
    # key converted to int
    key = int(argv[1])
    # check if the key was entered in properly checks to make sure a number is inputted and
    # checks if there is extra characters in

    try:
        (key == 0 and strncmp(argv[1], "0", true)) or len(sys.argv) > 3
    except IndexError:
        print("Usage: python " + sys.argv[0] + " k")
        return 0
    #ord() convert to in and chr converts to string

    name = input("plaintext: ")
    length = len(name)

    # converts key to modulus of 26 if person typed a larger number
    key = key % 26
    print("ciphertext: ", end="")
    for i in range(0, length):
        #checks if the name is lower case
        if ord(name[i]) > 96 and ord(name[i]) < 123:
            if (ord(name[i]) + key) % 122 < 97:
                print(chr(((ord(name[i]) + key) % 122) + 96), end="")
            else:
                print(chr(ord(name[i]) + key), end="")
        # checks if character is uppercase
        elif ord(name[i]) > 64 and ord(name[i]) < 91:
            if (ord(name[i]) + key) % 90 < 65:
                print(chr(((ord(name[i]) + key) % 90) + 65), end="")
            else:
                print(chr(ord(name[i]) + key), end="")
        # if it is non character it will just print
        else:
            print(name[i], end="")
    print("")
main(sys.argv)

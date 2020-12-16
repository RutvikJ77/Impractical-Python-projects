"""Generate silly names using file operations in python"""
import sys
import random

def main():
    '''This is a temporary random silly name generator game'''
    print("-----Welcome to the Pysch game to bewilder your mind-----\n")

    # Temporary names
    # first_lis = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
    # "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder',)
    # last_lis = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Cocktoasten',
    # 'Endicott', 'Fewhairs', 'Guster')

    #Loading data from names.txt
    names_file = open("names.txt", 'r')
    names = names_file.readlines()
    names_file.close()

    while True:
        first_name = random.choice(names)
        last_name = random.choice(names)
        print("\n")
        print(first_name + last_name, file=sys.stderr)
        print("\n")
        try_next = input("Not a suitable name? \nDo you want to try again (Y/N): ").lower()
        if try_next == "n":
            break

    input("\nPress enter to exit.")

if __name__ == "__main__":
    main()

import sys

def main():
    if len(sys.argv) == 1:
        print('enter messages')
    elif len(sys.argv) == 2 and sys.argv[1] == "?":
        print("with print command you can print out a string.")
    else:
        print(' '.join(sys.argv[1:]))

if __name__ == "__main__":
    main()
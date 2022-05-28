import sys

def main():
    if len(sys.argv) == 1:
        print('enter messages')
    else:
        print(' '.join(sys.argv[1:]))

if __name__ == "__main__":
    main()
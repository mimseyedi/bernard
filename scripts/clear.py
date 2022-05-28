import os
import sys

def main():
    if len(sys.argv) == 1:
        os.system("clear")
    elif len(sys.argv) == 2 and sys.argv[1] == "?":
        print("clean the screen.")

if __name__ == "__main__":
    main()
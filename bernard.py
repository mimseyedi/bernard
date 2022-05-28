"""
Bernard Version 1.0
Designed and written by Mohammad Seyedi

Bernard is a platform for executing Python scripts or subroutines
that come in the form of commands with different parameters.
Bernard has a central kernel that executes Python scripts
stored in a directory of the same name, and can also download and install scripts from the repository.

Bernard is open source under the MIT license and you can easily use it
and make any changes you like and share it with others.

Bernard github repository:
https://github.com/mimseyedi/bernard
"""

import os


def main():
    scripts_path = f"{os.getcwd()}/scripts"

    while True:
        current_directory = os.getcwd().split("/")[-1]
        command = input(f'➜ {current_directory}: ').strip()

        if len(command) > 0:
            main_command = command.split(' ')[0] + '.py'
            parameters = ' '.join(command.split(' ')[1:])

            if os.path.exists(f'{scripts_path}/{main_command}'):
                os.system(f'python {scripts_path}/{main_command} {parameters}')
            else:
                print(f'{main_command[:-3]} does not exist!')


if __name__ == "__main__":
    main()

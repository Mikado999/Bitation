import sys
import argparse

VERSION = '1.0'

class CommandLineInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Command Line Interface')
        self.parser.add_argument('--execute', type=str, help='Execute a specified file')
        self.parser.add_argument('--interactive', action='store_true', help='Start interactive shell')
        self.parser.add_argument('--debug', action='store_true', help='Enable debug mode')
        self.args = self.parser.parse_args()

    def execute_file(self, file_path):
        with open(file_path) as f:
            data = f.read()
            print(f'Executing file: {file_path}\n{data}')

    def start_interactive_shell(self):
        print('Starting interactive shell...')
        while True:
            command = input('> ')
            if command.lower() in ['exit', 'quit']:
                break
            if self.args.debug:
                print(f'Executing command: {command}')

    def run(self):
        if self.args.execute:
            self.execute_file(self.args.execute)
        elif self.args.interactive:
            self.start_interactive_shell()
        else:
            self.parser.print_help()

if __name__ == '__main__':
    cli = CommandLineInterface()
    cli.run()
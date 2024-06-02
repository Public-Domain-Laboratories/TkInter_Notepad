import argparse
import sys

class SilentArgParse(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'error: {message}\n')
        self.print_help()
        sys.exit(2)

    def print_help(self, file=None):
        if file is None:
            file = sys.stdout
        self._print_message(self.format_help(), file)

def main():
    parser = SilentArgParse(description='Example script with argparse')
    parser.add_argument('input', type=str, help='Input file')
    parser.add_argument('-o', '--output', type=str, help='Output file', default='output.txt')

    try:
        args = parser.parse_args()
    except SystemExit as e:
        # Handle error and help messages
        if e.code == 0:
            return
        else:
            raise

    # Your script logic here
    print(f'Input file: {args.input}')
    print(f'Output file: {args.output}')

if __name__ == "__main__":
    main()

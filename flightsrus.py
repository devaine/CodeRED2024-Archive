import argparse
import sys

parser = argparse.ArgumentParser(
    description="Taking the user's input within [prompt], we return the flight that will suit their needs."
)
parser.add_argument('[prompt]', help='Flight that you would like to take')
args = parser.parse_args()

def main():
    # Skip the first argument, which is the name of the script itself
    for arg in sys.argv[1:]:
        print(arg)
    else:
        parser.print_help()

main()

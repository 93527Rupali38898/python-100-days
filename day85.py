# command line utilies in python
import argparse

parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
parser.add_argument("output", help="Name of the output file")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(args.url)
print(args.output)

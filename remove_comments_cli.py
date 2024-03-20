#!/usr/bin/env python3

import os
import sys
import argparse

def main():
	# Take a file as input, then remove comments
	parser = argparse.ArgumentParser(description='Remove comments from a tex file')
	parser.add_argument('input', metavar='path to read', type=str, help='input file to read')
	parser.add_argument('-o', '--output', dest='output', default='-', type=str, help='output file to write', required=False)
	args = parser.parse_args()
	# Check if the input file exists
	if not os.path.exists(args.input):
		print('The file does not exist')
		exit(1)
	if args.output == '-':
		output_file = sys.stdout
	else:
		output_file = open(args.output, 'w')
	# Open the file and read it
	process_tex(args_input, output_file)
def process_tex(input, output):
	with open(input, 'r') as f:
		for line in f:
			# Remove comments
			if not line.startswith('%'):
				# Write to the output
				output.write(line)
	# Close the output file
	if output != sys.stdout:
		output.close()


if __name__ == '__main__':
	main()

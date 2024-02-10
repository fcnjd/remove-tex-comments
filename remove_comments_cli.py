#!/usr/bin/env python3

import os
import sys
import argparse
import chardet

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
	# Open the file and read it
	process_tex(args.input, args.output)

def process_tex(input, output):
	if output == '-':
		output_file = sys.stdout
	else:
		output_file = open(output, 'w')
	try:
		with open(input, 'rb') as f:
			raw_data = f.read()
			result = chardet.detect(raw_data)
			encoding = result['encoding']

		with open(input, 'r', encoding=encoding, errors='ignore') as f:
			for line in f:
				# Remove comments
				if not line.startswith('%'):
					# Write to the output
					output_file.write(line)
	finally:
		# Close the output file
		if output_file != sys.stdout:
			output_file.close()


if __name__ == '__main__':
	main()

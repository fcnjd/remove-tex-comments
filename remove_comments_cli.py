#!/usr/bin/env python3

import os
import sys
import argparse
import chardet

def main():
	# Take a file as input, then remove comments
	parser = argparse.ArgumentParser(description='Remove comments from a tex file')
	parser.add_argument('input', metavar='path to read', type=str, nargs='?', help='input file to read', default=None)
	parser.add_argument('-a', '--all', action='store_true', help='Process all .tex files in the specified directory or current directory if not specified')
	parser.add_argument('-o', '--output', dest='output', default='-', type=str, help='output file to write', required=False)
	args = parser.parse_args()
	if not args.input and not args.all:
		parser.error("You must specify an input file or use the '--all' option to process all .tex files in the current directory")
	if args.input and args.all:
		parser.error("The '--all' option cannot be used with a specific input file")
	file_count = 0
	if args.all:
		workdir = args.input if args.input else os.getcwd()  # Use specified directory or current directory
		target_dir = os.path.join(workdir, 'NoComments')
		os.makedirs(target_dir, exist_ok=True)  # Create target directory if it doesn't exist

		# Process each .tex file in the directory
		for filename in os.listdir(workdir):
			if filename.endswith('.tex'):
				input_path = os.path.join(workdir, filename)
				output_path = os.path.join(target_dir, filename)
				process_tex(input_path, output_path)
				file_count += 1
	else:
		if not os.path.exists(args.input):
			print('The file does not exist')
			exit(1)
		process_tex(args.input, args.output)
		file_count += 1
	print(f'Processed {file_count} file(s)')

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

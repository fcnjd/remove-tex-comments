# Tex Comment Remover

## Overview

Tex Comment Remover is a tool designed to help you clean up your `.tex` LaTeX files by removing comments. It offers both a Command Line Interface (CLI) and a Graphical User Interface (GUI), making it accessible to both programmers and non-programmers. This tool is especially useful for preparing `.tex` files for publication or sharing, where comments might not be desired.

## Features

- **CLI**: Allows for quick removal of comments from `.tex` files directly from the command line.
- **GUI**: Provides a simple and user-friendly graphical interface for removing comments from `.tex` files.

## CLI Documentation

### Installation

Ensure that Python 3 is installed on your system. To use the CLI, python scripts can be run directly.

### Usage

To use the CLI, navigate to the directory containing the script and run:

```bash
python3 tex_comment_remover.py [options]
```

#### Options
- **Input File Path**: Specify the path of the `.tex` file from which to remove comments. If this is not provided along with the `--all` option, it will default to the current directory.

    ```bash
    python3 tex_comment_remover.py input.tex
    ```

- **-a, --all**: Use this option to process all `.tex` files in the specified directory, or the current directory if no directory is specified. This option cannot be used with a specific input file.

    ```bash
    python3 tex_comment_remover.py --all
    ```

- **-o, --output**: Specify the output file where the processed content will be written. If not provided, the output will be printed to standard output.

    ```bash
    python3 tex_comment_remover.py input.tex -o output.tex
    ```

### Example

Remove comments from a specific `.tex` file and save the result in a specified output file:

```bash
python3 tex_comment_remover.py mypaper.tex -o cleaned_mypaper.tex
```

Process all `.tex` files in the current directory and store the cleaned files in a directory named `NoComments`:

```bash
python3 tex_comment_remover.py --all
```

## GUI Application

To use the GUI version, simply launch the executable file and use the provided interface to select files and remove comments.

## Downloads

A zip file containing the CLI script as well as the GUI Windows executable can be found in the Releases section of this repository. This makes it easy to use on systems without needing a Python environment set up.


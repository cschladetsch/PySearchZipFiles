# ZipFinder

A Python utility for recursively searching through zip files in a directory and finding files that match a specific pattern.

## Features

- Recursively traverses directories to find all zip files
- Lists the contents of zip files
- Searches for files within zip archives that match a regular expression pattern
- Verbose mode for detailed output
- Simple command-line interface

## Installation

No special installation is required beyond standard Python libraries. Simply download the script and make sure you have Python 3.6+ installed.

```bash
# Clone this repository or download the script
git clone https://github.com/yourusername/zipfinder.git
```

## Usage

```bash
python zipfinder.py [ROOT_FOLDER] [-p PATTERN] [-v]
```

### Arguments

- `ROOT_FOLDER`: Path to the root folder to search for zip files (required)
- `-p, --pattern`: Regular expression pattern to search for within zip files (optional)
- `-v, --verbose`: Verbose mode - show detailed listings of zip contents (optional)

### Examples

**List all matching files containing "backup" in their name:**
```bash
python zipfinder.py /path/to/search -p "backup"
```

**Search for all Python files in zip archives:**
```bash
python zipfinder.py /path/to/search -p "\.py$"
```

**Show detailed contents of all zip files while searching for PDF files:**
```bash
python zipfinder.py /path/to/search -p "\.pdf$" -v
```

**Search for files containing "STL" in the GoogleTakeout folder with verbose output:**
```bash
python zipfinder.py GoogleTakeout -p "STL" -v
```

## Output

In normal mode (without `-v`), the script only displays files that match the pattern:
```
/path/to/file1.zip: matching_file.txt
/path/to/file2.zip: another_match.pdf

Total zip files found: 15
Total files matching pattern 'pattern': 5
```

In verbose mode (with `-v`), the script shows the full contents of each zip file and highlights matches:
```
==================================================
Contents of: /path/to/file1.zip
==================================================
Searching for files matching pattern: 'pattern'
--------------------------------------------------
1. file1.txt
2. matching_file.txt (MATCH)
3. document.pdf

Found 1 matching files in this archive.

...

Total zip files found: 15
Total files matching pattern 'pattern': 5
```

## Error Handling

The script includes robust error handling for:
- Invalid zip files
- Non-existent directories
- Permission issues
- General exceptions during file operations

## Requirements

- Python 3.6 or higher
- Standard libraries: os, re, zipfile, argparse, pathlib

## License

[MIT License](LICENSE)

## Contributing

Contributions, issues, and feature requests are welcome!

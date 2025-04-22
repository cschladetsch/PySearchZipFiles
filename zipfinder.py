import argparse
import os
import re
import zipfile
from pathlib import Path


def find_and_read_zip_files(root_folder, pattern=None, verbose=False):
    """
    Traverses the given root folder for zip files, lists their contents,
    and optionally searches for files matching a regex pattern.
    
    Args:
        root_folder (str): Path to the root folder to start traversal
        pattern (str, optional): Regular expression pattern to search for
        verbose (bool): Whether to print detailed file listings
    """
    # Convert to Path object for easier handling
    root_path = Path(root_folder)
    
    # Check if the provided path exists
    if not root_path.exists():
        print(f"Error: The path '{root_folder}' does not exist.")
        return
    
    # Compile regex pattern if provided
    regex = re.compile(pattern) if pattern else None
    
    # Keep track of zip files and matches found
    zip_count = 0
    total_matches = 0
    
    # Walk through all subdirectories
    for dirpath, _dirnames, filenames in os.walk(root_path):
        # Filter for zip files
        zip_files = [f for f in filenames if f.lower().endswith('.zip')]
        
        for zip_file in zip_files:
            zip_count += 1
            full_path = Path(dirpath) / zip_file
            
            if verbose:
                print(f"\n{'='*50}")
                print(f"Contents of: {full_path}")
                print(f"{'='*50}")
            
            try:
                # Open the zip file
                with zipfile.ZipFile(full_path, 'r') as zip_ref:
                    # Get list of file names
                    file_list = zip_ref.namelist()
                    
                    if file_list:
                        match_count = 0
                        
                        if pattern and verbose:
                            print(f"Searching for files matching pattern: '{pattern}'")
                            print(f"{'-'*50}")
                        
                        for i, file_name in enumerate(file_list, 1):
                            if not pattern:
                                if verbose:
                                    # Just list all files if no pattern specified
                                    print(f"{i}. {file_name}")
                            elif regex.search(file_name):
                                # File matches the pattern
                                match_count += 1
                                total_matches += 1
                                print(f"{full_path}: {file_name}")
                        
                        if pattern and verbose:
                            if match_count == 0:
                                print("No matching files found in this archive.")
                            else:
                                print(f"\nFound {match_count} matching files in this archive.")
                    elif verbose:
                        print("(empty zip file)")
            except zipfile.BadZipFile:
                print(f"Error: '{full_path}' is not a valid zip file.")
            except Exception as e:
                print(f"Error reading '{full_path}': {str(e)}")
    
    print(f"\nTotal zip files found: {zip_count}")
    if pattern:
        print(f"Total files matching pattern '{pattern}': {total_matches}")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Search for zip files and optionally find files within them matching a pattern.'
    )
    
    parser.add_argument('root', help='Root folder path to search for zip files')
    parser.add_argument(
        '-p', '--pattern', help='Regular expression pattern to search for within zip files'
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='Verbose mode - show detailed listings of zip contents'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the main function with provided arguments
    find_and_read_zip_files(args.root, args.pattern, verbose=args.verbose)


if __name__ == "__main__":
    main()

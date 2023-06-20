Stratford Email Extractor is a robust email extraction tool created by Vincent Alize and powered by Stratford IT Solutions.
It has been designed to efficiently scan through directories and subdirectories, extracting email addresses from text files, SQL files, and CSV files.
Features

    Encoding detection: The extractor incorporates encoding detection to prevent decoding errors, allowing it to handle a variety of file types with different encoding standards.
    Directory traversal: You can provide the path to a directory and the extractor will automatically traverse through all the files and subdirectories.
    File size management: All the extracted unique emails are written into a CSV file. However, to manage large amounts of data, the extractor divides the output into multiple files, with each file not exceeding 19.5MB.
    Email extraction: The tool uses a case-insensitive regular expression to accurately and efficiently extract emails from files.
    Duplicate handling: It ensures there are no duplicate emails in the output files, offering a clean list of unique email addresses.

Usage

The tool is a Python script, which can be run from the command line:

bash

python email_extractor.py -d /path/to/directory -o output

Here, -d or --directory is the directory to be scanned, and -o or --output is the base name for the output files.
Dependencies

This tool uses the following Python libraries:

    os
    re
    argparse
    csv
    chardet

To install the required libraries, run:

bash

pip install chardet

The other libraries are part of Python's standard library and should not require separate installation.
Ethical Use

This tool is intended for ethical use only. Please respect privacy and always follow ethical guidelines and legal regulations when handling personal data such as email addresses.

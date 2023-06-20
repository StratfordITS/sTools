import os
import re
import argparse
import pandas as pd
import chardet
import csv

def extract_emails_from_file(file_path):
    try:
        # Detecting the file encoding
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
        
        # Reading the file with the detected encoding
        with open(file_path, 'r', encoding=result['encoding']) as file:
            data = file.read()
        
        # Regular expression pattern for detecting emails
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # re.IGNORECASE makes the regex pattern case-insensitive
        emails = re.findall(email_pattern, data, re.IGNORECASE)
        return emails
    except Exception as e:
        print(f"Error with file: {file_path}. Error message: {str(e)}. Skipping...")
        return []

def extract_emails_from_directory(dir_path, base_output_filename):
    emails = []
    
    # Walk through each file in the directory and subdirectories
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # Only process .txt, .sql, .csv files
            if file.endswith(('.txt', '.sql', '.csv')):
                file_path = os.path.join(root, file)
                emails.extend(extract_emails_from_file(file_path))
    
    # Define file limit size in bytes (20MB)
    FILE_SIZE_LIMIT = 19.5 * 1024 * 1024

    # Writing unique emails to the output files
    unique_emails = list(set(emails))

    file_index = 0
    output_filename = f"{base_output_filename}_{file_index}.csv"
    with open(output_filename, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Emails"])  # write header
        for email in unique_emails:
            writer.writerow([email])
            output_file.flush()  # make sure it's written to disk
            if os.path.getsize(output_filename) > FILE_SIZE_LIMIT:
                # Current file reached size limit, close it and open a new one
                file_index += 1
                output_filename = f"{base_output_filename}_{file_index}.csv"
                output_file = open(output_filename, 'w')
                writer = csv.writer(output_file)
                writer.writerow(["Emails"])  # write header

def print_logo_and_author():
    print("""
    _____ _               _   _ ________   __             
   / ____| |             | | (_)  ____\ \ / /             
  | (___ | |_ _ __ _   _| |_ _| |__   \ V /____ _ _ __   
   \___ \| __| '__| | | | __| |  __|   > < _____| '__|  
   ____) | |_| |  | |_| | |_| | |____ / . \_____| |     
  |_____/ \__|_|   \__,_|\__|_|______/_/ \_\_____|_|    
  Program Author: Vincent Alize
  Information Scraping Tool
    """)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract email addresses from files in a directory.')
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory to search for files.')
    parser.add_argument('-o', '--output', type=str, required=True, help='Base output CSV file to store emails.')

    args = parser.parse_args()

    print_logo_and_author()
    print("\nStarting email extraction from directory: " + args.directory)
    extract_emails_from_directory(args.directory, args.output)
    print("Email extraction completed. Output files: " + args.output + "_*.csv")

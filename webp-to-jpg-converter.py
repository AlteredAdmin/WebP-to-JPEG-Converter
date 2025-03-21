#!/usr/bin/env python3

import os
import time
from datetime import datetime
from PIL import Image

def check_and_clean_log(directory, log_filename, days_threshold=30):
    """
    Check if the log file exists in the directory.
    If it exists and is older than days_threshold days, delete it.
    Returns the full path to the log file.
    """
    log_path = os.path.join(directory, log_filename)
    if os.path.exists(log_path):
        last_modified_time = os.path.getmtime(log_path)
        # Convert threshold to seconds (30 days)
        if time.time() - last_modified_time > days_threshold * 24 * 3600:
            os.remove(log_path)
            print(f"Deleted old log file: {log_path}")
    return log_path

def convert_webp_to_jpg(directory, log_filename='conversion.log'):
    """
    Converts all .webp images in the given directory to .jpg format.
    Logs the conversion process in a log file in the same directory.
    """
    # Verify the directory exists
    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Check and clean the log file if necessary
    log_path = check_and_clean_log(directory, log_filename)

    # Open the log file for appending
    with open(log_path, 'a') as log_file:
        start_time = datetime.now()
        log_file.write(f"Conversion started at {start_time}\n")
        print(f"Conversion started at {start_time}")

        # Loop through each file in the directory
        for filename in os.listdir(directory):
            if filename.lower().endswith('.webp'):
                webp_path = os.path.join(directory, filename)
                jpg_filename = os.path.splitext(filename)[0] + '.jpg'
                jpg_path = os.path.join(directory, jpg_filename)
                
                try:
                    # Open the .webp image, convert it to RGB, and save as .jpg
                    with Image.open(webp_path) as img:
                        rgb_img = img.convert('RGB')
                        rgb_img.save(jpg_path, 'JPEG')
                    message = f"Converted '{webp_path}' to '{jpg_path}'"
                    print(message)
                    log_file.write(message + "\n")
                except Exception as e:
                    error_message = f"Error converting '{webp_path}': {e}"
                    print(error_message)
                    log_file.write(error_message + "\n")
        
        end_time = datetime.now()
        log_file.write(f"Conversion ended at {end_time}\n\n")
        print(f"Conversion ended at {end_time}")

if __name__ == '__main__':
    # Replace with the path to your directory containing .webp images
    target_directory = 'path/to/your/directory'
    convert_webp_to_jpg(target_directory)

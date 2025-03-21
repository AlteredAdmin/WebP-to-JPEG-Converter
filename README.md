# WebP to JPEG Converter

This utility converts all `.webp` images in a specified directory to `.jpg` format using the Pillow library. It logs every conversion step to a log file in the same directory and automatically deletes the log if it is older than 30 days.

## Features

- **Image Conversion:** Converts `.webp` images to `.jpg` by converting them to RGB before saving.
- **Logging:** Generates a log file (`conversion.log`) that records the start and end time of the conversion process, along with details of each conversion or any errors encountered.
- **Log Maintenance:** Automatically checks and deletes the log file if it is older than 30 days, ensuring that logs remain up-to-date.

## Requirements

- Python 3.x
- Pillow
  Install via pip:
  ```bash
  pip install Pillow
  ```

## Usage

1. **Configure the Script:**
   - Open `webp-to-jpg-converter.py` in your preferred text editor.
   - Replace the placeholder for `target_directory` with the actual path to the directory containing your `.webp` images.

2. **Run the Script:**
   ```bash
   python webp-to-jpg-converter.py
   ```

3. **Check the Log:**
   - A file named `conversion.log` will be created (or updated) in the target directory.
   - If this log is older than 30 days, it will be deleted before a new conversion session begins.

## Customization

- **Log Filename:**  
  You can change the log file name by modifying the `log_filename` parameter in the `convert_webp_to_jpg` function.
  
- **Log Retention Period:**  
  To adjust the age threshold for log deletion, change the `days_threshold` parameter in the `check_and_clean_log` function.

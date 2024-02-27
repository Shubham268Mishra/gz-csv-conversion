import os
import gzip
import csv


# Function to unzip .gz file and convert to CSV
def unzip_and_convert_to_csv(input_file, output_file):
    with gzip.open(input_file, "rt") as f_in:
        with open(output_file, "w", newline="") as f_out:
            # Read the content and split it into lines
            content = f_in.read()
            lines = content.split("\n")

            # Create a CSV writer
            csv_writer = csv.writer(f_out)

            # Write each line as a row in the CSV file
            for line in lines:
                csv_writer.writerow([line])


# Define the path to the main folder containing gzipped files
main_folder = r"folder_path"


# Function to process all .gz files in the specified folder
def process_gz_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".gz"):
                gzipped_file_path = os.path.join(root, file)
                csv_output_file = os.path.join(root, file[:-3] + ".csv")
                # Output CSV file path
                unzip_and_convert_to_csv(gzipped_file_path, csv_output_file)


# Call the function to process all .gz files in the main folder
process_gz_files_in_folder(main_folder)

print("Unzipping and conversion to CSV complete!")

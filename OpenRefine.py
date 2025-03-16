import subprocess
from time import sleep
from common_lib import *

#
app_name = 'OpenRefine'

import zipfile
import os


def extract_zip(zip_file_path, extract_to_folder):
    # Check if the ZIP file exists
    if not os.path.exists(zip_file_path):
        print(f"The file {zip_file_path} does not exist.")
        return

    # Check if the destination folder exists, if not, create it
    if not os.path.exists(extract_to_folder):
        os.makedirs(extract_to_folder)

    # Open the ZIP file and extract its contents
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)
        print(f"Contents extracted to {extract_to_folder}")


def list_files_and_dirs(directory):
    file_list=[]
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return None

    # List all files and directories
    for root, dirs, files in os.walk(directory):
        # for dir_name in dirs:
        #     print(f"  Directory: {dir_name}")
        for file_name in files:
            # print(f"  File: {file_name}")
            file_list.append(file_name)
    return file_list


def OpenRefine(app_name, file_name_exe, download_link):
    app_name = 'OpenRefine'
    try:
        # Check app is installed
        result = check_app_existed(app_name)
        if result:
            return True
        # tao folder luu file tai ve
        download_directory = f'{get_download_folder()}\{app_name}'
        make_folder_log(download_directory)
        # Download and execute install file
        download_result = download_app(download_directory, download_link)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result
        # Get a list of files in the folder
        file_names = os.listdir(download_directory)

        # Filter out installer files
        install_files = [file for file in file_names if
                         (file.lower().endswith('.exe') or file.lower().endswith('.msi') or file.lower().endswith('.zip')) and os.path.isfile(
                             os.path.join(download_directory, file))]
        if '.zip' in install_files[0].lower():
            # Example usage
            zip_file = f"{download_directory}\{install_files[0]}"  # Replace with your ZIP file path
            extract_to = f"{download_directory}"  # Replace with the folder to extract the files
            extract_zip(zip_file, extract_to)

        # Filter out installer files
        # Example usage
        directory_path = download_directory  # Replace with your directory path
        list_files = list_files_and_dirs(directory_path)
        if ['openrefine.exe' in file for file in list_files]:
            print('pass')
            return True
        else:
            return False
    except Exception as e:
        print(f'error install: {e}')
        return False


# if __name__ == '__main__':
#     download_link = 'https://github.com/OpenRefine/OpenRefine/releases/download/3.9.0/openrefine-win-with-java-3.9.0.zip'
#     OpenRefine(app_name, '', download_link)

    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

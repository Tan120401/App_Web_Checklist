import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_and_execute, check_program_installed, connect_app, \
    click_object


def Google_Drive(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 30, 5)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        #Connect app
        target_window = connect_app('Google Drive')
        click_object(target_window, '', '301', 'Button')
        sleep(5)
        click_object(target_window, '', '303', 'Button')
        sleep(10)
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Google_Drive('Google Drive', 'GoogleDriveSetup.exe', 'https://dl.google.com/drive-file-stream/GoogleDriveSetup.exe')
print(result)
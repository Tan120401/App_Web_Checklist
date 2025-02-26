import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_and_execute, check_program_installed, connect_app, \
    click_object

def OneDrive(app_name, file_name_exe, download_link):
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

        sleep(12)
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

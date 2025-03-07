import os

from time import sleep

from common_lib import check_program_installed, download_and_execute

def IPinsideLWS(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('IPinside LWS Agent')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Check app installed
        for i in range(36):
            result = check_program_installed('IPinside LWS Agent')
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

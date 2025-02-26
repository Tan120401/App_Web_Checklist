import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, check_program_installed, download_and_execute


def IPinsideLWS(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('IPinside LWS Agent')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 20, 10)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        #
        # # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed('IPinside LWS Agent')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
IPinsideLWS()
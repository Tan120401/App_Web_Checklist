import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_and_execute, connect_app, click_object, \
    check_program_installed, close_app


def TouchEnNxKey(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('TouchEn nxKey')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 5)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Check app installed
        for i in range(36):
            result = check_program_installed('TouchEn nxKey')
            if result:
                close_app('TouchEn nxKey')
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False
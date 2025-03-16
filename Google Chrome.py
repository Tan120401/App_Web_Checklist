import os

from time import sleep

from common_lib import download_by_link, run_file_exe, click_by_xpath, download_and_execute, connect_app, click_object, \
    check_program_installed, download_directory, click_without_id, close_app, print_all_windows, click_without_title


def Google_Chrome(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 5)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                sleep(10)
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

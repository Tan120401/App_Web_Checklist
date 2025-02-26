import os
from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    click_without_id, click_object


def PokerStars(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10, 10)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('Setup PokerStars')
        click_object(target_window, 'I agree to terms of the PokerStars ', '151', 'CheckBox')
        click_without_id(target_window, 'I', 'Button')
        click_without_id(target_window, 'L', 'Button')
        #Click next

        #Wait for installation
        sleep(5)
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

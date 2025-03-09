import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, connect_app, print_all_windows, click_object, \
    check_program_installed, click_without_id, download_and_execute


def Wizin_Delfino_G3(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('Delfino G3')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 5)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result
        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Delfino G3')

        #Click next
        click_without_id(target_window, 'Next >', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed('Delfino G3')
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

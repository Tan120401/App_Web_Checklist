import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_and_execute, connect_app, check_program_installed, \
    click_object, click_without_id, click_object_by_index

def Gom_Audio(app_name, file_name_exe, download_link):
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

        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Installer Language')

        #Click ok
        click_object(target_window, 'OK', '1', 'Button')
        sleep(10)

        setup_window = connect_app('GOM Audio Setup')
        #Click ok
        click_object(setup_window, 'Next >', '1', 'Button')
        click_object(setup_window, 'I Agree', '1', 'Button')
        click_object(setup_window, 'Next >', '1', 'Button')
        click_object(setup_window, 'Next >', '1', 'Button')
        click_object_by_index(setup_window, 'Close', 'Button', 0)

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

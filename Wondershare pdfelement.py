import os

from time import sleep

from pywinauto import Application

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_without_id, download_exe_file, install_app


def Wondershare_pdfelement(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download file
        file_path = download_exe_file(file_name_exe, download_link)
        print(file_path)
        if file_path:
            # Install app
            install_app(file_path, "/S")
        else:
            print('Time out')
            return False

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            print('ket qua:', result)
            sleep(5)
    except Exception as e:
        print(f'error install: {e}')
        return False

import os

from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, connect_app, download_and_execute, \
    download_exe_file, install_app_by_cmd


def DWG_FastView(app_name, file_name_exe, download_link):
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
            install_app_by_cmd(file_path, "/S")
        else:
            print('Time out')
            return False

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(5)
    except Exception as e:
        print(f'error install: {e}')
        return False

import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, connect_app, click_object, \
    check_program_installed, download_and_execute, download_exe_file, install_app_by_cmd


def CrossWeb_EX(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download file
        file_path = download_exe_file(file_name_exe, download_link)
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
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

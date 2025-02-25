import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, connect_app, click_object, \
    check_program_installed, download_and_execute


def CrossWebEX(app_name, file_name_exe, download_link):
    try:
        result = download_and_execute(app_name, file_name_exe, download_link, 60, 10)
        if result:
            return result
        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('CrossWeb EX')

        #Click close
        click_object(target_window, 'Close', '', 'Button')

        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

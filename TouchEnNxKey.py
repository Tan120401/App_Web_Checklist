import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_and_execute, connect_app, click_object, \
    check_program_installed, close_app


def TouchEnNxKey(app_name, file_name_exe, download_link):
    try:
        result = download_and_execute('TouchEn nxKey', file_name_exe, download_link, 60, 10)

        if result:
            return result
        sleep(12)
        # Kết nối tới màn hình cài đặt app
        close_app('TouchEn nxKey')

        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed('TouchEn nxKey')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
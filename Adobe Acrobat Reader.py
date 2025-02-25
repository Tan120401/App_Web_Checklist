import os

from time import sleep

from common_lib import download_and_execute, connect_app, click_object, check_program_installed


def Adobe_Acrobat_Reader(app_name, file_name_exe, download_link):
    try:
        result = download_and_execute('Adobe Acrobat', file_name_exe, download_link, 10, 120)
        if result:
            return result
        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Adobe Acrobat Reader Installer')
        # Click finished
        click_object(target_window, 'Finish', 'primary-button', 'Button')
        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed('Adobe Acrobat')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

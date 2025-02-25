import os

from time import sleep

from common_lib import download_by_link, run_file_exe, click_by_xpath, download_and_execute, connect_app, click_object, \
    check_program_installed, download_directory, click_without_id


def Adobe_Creative_Cloud(app_name, file_name_exe, download_link):
    try:
        # result = download_and_execute(app_name, file_name_exe, download_link, 10, 5)
        # if result:
        #     return result
        # Kết nối tới màn hình cài đặt app
        target_window = connect_app(app_name)
        # Click finished
        click_without_id(target_window, 'Continue', 'Button')
        sleep(20)
        click_without_id(target_window, 'Start installing', 'Button')
        click_without_id(target_window, 'Skip question', 'Button')
        click_without_id(target_window, 'Skip question', 'Button')
        sleep(90)
        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

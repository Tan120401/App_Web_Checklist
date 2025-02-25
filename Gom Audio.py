import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_and_execute, connect_app, check_program_installed, \
    click_object, click_without_id, click_object_by_index


def Gom_Audio(app_name, file_name_exe, download_link):
    try:
        result = download_and_execute(app_name, file_name_exe, download_link, 20, 5)

        if result:
            return result
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
        print(setup_window.print_control_identifiers())
        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
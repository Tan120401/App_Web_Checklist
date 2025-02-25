import os

from time import sleep

from common_lib import download_by_link, run_file_exe, click_by_xpath, download_and_execute, check_program_installed, \
    connect_app, click_object


def Melon_Player(app_name, file_name_exe, download_link):
    try:
        result = download_and_execute(app_name, file_name_exe, download_link, 30, 5)
        if result:
            return result
        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Melon Player')
        click_object(target_window, '동의함', '1','Button')
        click_object(target_window, '설치', '1','Button')
        sleep(20)
        click_object(target_window, '마침', '1','Button')

        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

result = Melon_Player('Melon Player', 'MelonSetup.exe', 'https://cdnstatic.melon.co.kr/svc/pcp/apps/w10/MelonSetup.exe')
print(result)
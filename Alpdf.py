import os

from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_directory, \
    get_latest_file, connect_app, click_by_xpath, print_all_windows, click_without_id, close_app, get_link, \
    download_and_execute

def Alpdf(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('알PDF')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 5)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        #Connect app
        target_window = connect_app('Setup - 알PDF')
        click_without_id(target_window,'Agree(A)', 'Button')
        sleep(30)

        almain_window = connect_app('알매니저')
        click_without_id(almain_window, '설치를 시작합니다.', 'Button')
        sleep(15)
        click_without_id(almain_window, '제품 실행', 'Button')
        click_without_id(almain_window, '동의 후 설치', 'Button')
        close_app('알PDF')
        click_without_id(almain_window, '취소', 'Button')
        close_app('알매니저')

        # Check app installed
        for i in range(24):
            result = check_program_installed('알PDF')
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False
Alpdf('Alpdf', 'ALPDF403.exe', 'https://advert.estsoft.com/?event=201601201427327')
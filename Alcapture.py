from time import sleep

from pywinauto import Desktop

from common_lib import download_by_link, run_file_exe, download_directory, connect_app, check_program_installed, \
    download_and_execute, print_all_windows, click_without_id


def Alcapture(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('알캡처')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 5)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('Setup - 알캡처')
        click_without_id(target_window, 'Agree(A)', 'Button')
        almain_window = None
        for i in range(10):
            almain_window = connect_app('알매니저')
            if almain_window:
                break
            sleep(5)

        click_without_id(almain_window, '설치를 시작합니다.', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed('알캡처')
            if result:
                sleep(5)
                click_without_id(almain_window, '확인', 'Button')
                almain_window.close()
                return result
            sleep(5)
    except Exception as e:
        print(f'error app: {e}')
        return False

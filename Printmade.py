import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, check_program_installed, print_all_windows


from common_lib import  connect_app, \
    click_object, check_program_installed, download_and_execute

def Printmade(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 20, 5)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Setup')
        # Click next
        click_object(target_window, 'Yes', '6', 'Button')
        sleep(10)
        click_object(target_window, 'OK', '2', 'Button')
        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
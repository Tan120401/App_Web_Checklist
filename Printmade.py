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
        download_result = download_and_execute(file_name_exe, download_link, 5)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Setup')
        # Click next
        click_object(target_window, 'Yes', '6', 'Button')
        sleep(10)
        click_object(target_window, 'OK', '2', 'Button')

        #Check app installed
        for i in range(36):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False
import os
from time import sleep
from common_lib import download_directory, connect_app, check_program_installed, \
    download_and_execute, print_all_windows, click_without_id, click_object, download_by_link, click_by_xpath, \
    get_latest_file, run_file_exe

def Ahnlab_V3_Lite(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 30)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('AhnLab V3 Lite Setup')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'I agree to the terms of the license agreement', 'CheckBox')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'I agree', 'CheckBox')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'Install', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                sleep(5)
                target_window.close()
                return result
            sleep(10)
    except Exception as e:
        print(f'error app: {e}')
        return False

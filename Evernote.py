import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_and_execute, check_program_installed, connect_app, \
    click_object

def Evernote(app_name, file_name_exe, download_link):
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

        # wait for install done
        target_window = connect_app('Evernote Setup')
        click_object(target_window, 'I accept the terms in the License Agreement', '1034', 'CheckBox')
        click_object(target_window, 'Next >', '1', 'Button')
        click_object(target_window, 'Install', '1', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

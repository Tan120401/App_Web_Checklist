import os
from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, connect_app, \
    click_object, check_program_installed, download_exe_file, install_app, download_and_execute, print_all_windows, \
    click_without_id


def Ahnlab_Safe_Transaction(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10, 90)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result


        #Connect app
        target_window = connect_app('AhnLab Safe Transaction Setup')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'I Agree', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(5)
    except Exception as e:
        print(f'App handle error: {e}')
        return  False

result = Ahnlab_Safe_Transaction('Ahnlab Safe Transaction', 'astxdn.exe', 'https://bank.shinhan.com/sw/astx/astxdn.exe')
print(result)
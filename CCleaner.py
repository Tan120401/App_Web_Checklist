import os
from time import sleep
from common_lib import download_directory, connect_app, check_program_installed, \
    download_and_execute, print_all_windows, click_without_id, click_object, download_by_link, click_by_xpath, \
    get_latest_file, run_file_exe

def CCleaner(app_name, file_name_exe, download_link):
    try:
        # # Check app is installed
        # result = check_program_installed(app_name)
        # if result:
        #     return result
        #
        # # Download and execute install file
        # download_result = download_and_execute(file_name_exe, download_link, 20, 10)
        #
        # # If download and execute fail -> return fail
        # if not download_result:
        #     return download_result

        # Connect app
        target_window = connect_app('CCleaner Installation')
        print(target_window.print_control_identifiers())

        # Check app install
        return True
    except Exception as e:
        print(f'error app: {e}')
        return False
result = CCleaner('CCleaner','ccsetup633.exe','https://www.ccleaner.com/ccleaner/download/standard')
print(result)
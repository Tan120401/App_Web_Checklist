import os

from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, connect_app, download_and_execute

def DWG_FastView(app_name, file_name_exe, download_link):
    try:
        # # Check app is installed
        # result = check_program_installed(app_name)
        # if result:
        #     return result
        #
        # # Download and execute install file
        # download_result = download_and_execute(file_name_exe, download_link, 15, 10)
        #
        # # If download and execute fail -> return fail
        # if not download_result:
        #     return download_result

        # Connect app
        target_window = connect_app('DWG')
        print(target_window.print_control_identifiers())
        # Check app install
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
DWG_FastView('DWG FastView', 'DWGFastView(KR-1)_x64_1.exe', 'https://dwgfastview-bsyun.dwgfastview.com/Download/KR/8.8/DWGFastView%28KR-1%29_x64_1.exe')
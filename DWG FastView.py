import os

from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, connect_app, download_and_execute, \
    download_exe_file, install_app


def DWG_FastView(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download file
        file_path = download_exe_file(file_name_exe, download_link, 15)
        print(file_path)
        if file_path:
            # Install app
            install_app(file_path, "/S")
        else:
            print('Time out')
            return False

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            print('ket qua:', result)
            sleep(5)
    except Exception as e:
        print(f'error install: {e}')
        return False
DWG_FastView('DWG FastView', 'DWGFastView(KR-1)_x64_1.exe', 'https://dwgfastview-bsyun.dwgfastview.com/Download/KR/8.8/DWGFastView%28KR-1%29_x64_1.exe')
import os

from time import sleep

from pywinauto import Application

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_without_id, download_exe_file, install_app


def Wondershare_pdfelement(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download file
        file_path = download_exe_file(file_name_exe, download_link, 10)
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

Wondershare_pdfelement('Wondershare pdfelement', 'pdfelement-pro_setup_full5239.exe', 'https://download.wondershare.com/pdfelement-pro_full5239.exe?_gl=1*15dl66l*_ga*OTQ2NTk5MDE3LjE3NDAzNjE2MzQ.*_ga_24WTSJBD5B*MTc0MDM2MTYzMy4xLjAuMTc0MDM2MTYzNS42MC4wLjE2NDIwNDk4NQ..*_gcl_au*MTc0MTcxMjM3MC4xNzQwMzYxNjM2')
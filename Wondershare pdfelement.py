import os

from time import sleep

from pywinauto import Application

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_without_id


def Wondershare_pdfelement(app_name, file_name_exe, download_link):
    try:
        # # Check app is installed
        # result = check_program_installed(app_name)
        # if result:
        #     return result
        #
        # # Download and execute install file
        # download_result = download_and_execute(file_name_exe, download_link, 10, 10)
        #
        # # If download and excute fail -> return fail
        # if not download_result:
        #     return download_result

        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('PDFelement11')
        click_without_id(target_window, 'Install', 'Text')
        print(target_window.print_control_identifiers(depth=2))
        # Click Continue

        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

Wondershare_pdfelement('Wondershare pdfelement', 'pdfelement-pro_setup_full5239.exe', 'https://download.wondershare.com/pdfelement-pro_full5239.exe?_gl=1*15dl66l*_ga*OTQ2NTk5MDE3LjE3NDAzNjE2MzQ.*_ga_24WTSJBD5B*MTc0MDM2MTYzMy4xLjAuMTc0MDM2MTYzNS42MC4wLjE2NDIwNDk4NQ..*_gcl_au*MTc0MTcxMjM3MC4xNzQwMzYxNjM2')
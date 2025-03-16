import os

from time import sleep


from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_without_id, download_exe_file, install_app_by_cmd, click_object_by_image, close_app

def Wondershare_pdfelement(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download file
        file_path = download_and_execute(file_name_exe, download_link, 5)

        target_window = connect_app('PDFelement11')
        print(target_window.print_control_identifiers())

        #Click agree
        check_box_path = r'Resource/image/check_box.png'
        click_object_by_image(check_box_path, 0.8)

        #Click Install
        install_path = r'Resource/image/wondershare_install.png'
        click_object_by_image(install_path)

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                sleep(5)
                close_app('PDFelement11')
                return result
            print('ket qua:', result)
            sleep(5)
    except Exception as e:
        print(f'error install: {e}')
        return False

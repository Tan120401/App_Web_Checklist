import os
from time import sleep
from common_lib import download_directory, connect_app, check_program_installed, \
    download_and_execute, print_all_windows, click_without_id, click_object, download_by_link, click_by_xpath, \
    get_latest_file, run_file_exe, click_object_by_image

def FiveKPlayer(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('5KPlayer')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 30)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('5KPlayerinstall')
        install_path = r'Resource/image/5KPlayer/install.png'
        click_object_by_image(install_path, 0.8)



        # Check app installed
        for i in range(24):
            result = check_program_installed('5KPlayer')
            if result:
                sleep(10)
                target_window.close()
                return result
            sleep(10)
    except Exception as e:
        print(f'error app: {e}')
        return False

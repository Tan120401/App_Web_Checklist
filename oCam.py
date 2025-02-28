import os
from time import sleep
from common_lib import download_directory, connect_app, check_program_installed, \
    download_and_execute, print_all_windows, click_without_id, click_object, download_by_link, click_by_xpath, \
    get_latest_file, run_file_exe


def oCam(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            # Download by link
            driver = download_by_link(download_link)

            # Click Download
            click_by_xpath(driver, '/html/body/table[2]/tbody/tr[1]/td[3]/button')
            sleep(10)

            file_path = get_latest_file()
        run_file_exe(file_path)

        #Select language
        language_window = connect_app('Select Setup Language')
        click_without_id(language_window, 'OK', 'Button')
        sleep(2)

        #Connect app
        target_window = connect_app('Setup - oCam')
        click_without_id(target_window, 'I accept the agreement', 'RadioButton')
        click_without_id(target_window, 'Next >', 'Button')
        sleep(10)
        #Check install app
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error app: {e}')
        return False

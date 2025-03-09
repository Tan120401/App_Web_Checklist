import os
from time import sleep

from pyautogui import click

from common_lib import check_program_installed, download_and_execute, \
    connect_app, download_by_link, click_by_xpath, print_all_windows, get_latest_file, run_file_exe, download_directory, \
    click_without_id, click_object

def Polaris_Office(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            # Download file
            driver = download_by_link(download_link)

            #click download
            click_by_xpath(driver, '//*[@id="personal"]/div[1]/div[2]/div[1]/div/div/a[1]')
            sleep(60)

            # Get latest file
            file_path = get_latest_file()

        # Run file exe
        run_file_exe(file_path)
        sleep(30)

        #Connect app
        target_window = connect_app('Polaris Office Installation')
        click_object(target_window, 'Agree and Install', '1025','Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

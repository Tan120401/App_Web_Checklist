import os
from time import sleep

from common_lib import check_program_installed, download_and_execute, \
    connect_app, download_by_link, click_by_xpath, print_all_windows, get_latest_file, run_file_exe, download_directory, \
    click_without_id, click_object, check_app_installed, get_link


def Zoom(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_app_installed(app_name)
        if result:
            return result
        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            # Download file
            driver = get_link(download_link)

            #Click Download
            click_by_xpath(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]/a[1]')
            #Wait for download
            sleep(30)
            driver.quit()
            # Get latest file
            file_path = get_latest_file()

        # Run file exe
        run_file_exe(file_path)
        sleep(20)

        # Check app installed
        for i in range(24):
            result = check_app_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

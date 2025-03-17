import os
from time import sleep

from common_lib import check_program_installed, download_and_execute, \
    connect_app, download_by_link, click_by_xpath, print_all_windows, get_latest_file, run_file_exe, download_directory, \
    click_without_id, click_object, get_link


def KMPlayer(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Check file install is existed
        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            # Download file
            driver = get_link(download_link)
            #Close popup
            click_by_xpath(driver, '//*[@id="layer2"]/div/div[2]/label/div[2]/close')
            sleep(2)
            click_by_xpath(driver, '//*[@id="container"]/div[1]/div[1]/div[2]/a[1]')
            sleep(5)
            #Click Download
            click_by_xpath(driver, '//*[@id="layer2"]/div/div[1]/div[1]/div[2]/div[2]/div[2]/a[2]')
            #Wait for download
            sleep(10)
            driver.quit()
            # Get latest file
            file_path = get_latest_file()

        # Run file exe
        run_file_exe(file_path)
        sleep(5)

        #Select language
        select_language_window = connect_app('Installer Language')
        click_without_id(select_language_window, 'OK', 'Button')
        sleep(5)

        # Connect setup app
        target_window = connect_app('KMPlayer')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'I Agree', 'Button')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'Install', 'Button')
        sleep(12)
        click_without_id(target_window, 'Finish', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

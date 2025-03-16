import os
from time import sleep
from common_lib import check_program_installed, download_exe_file, install_app_by_cmd, get_latest_file, click_by_xpath, \
    get_link


def BAND(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        driver = get_link(download_link)

        sleep(5)

        # Click download
        click_by_xpath(driver, '/html/body/div[4]/div/div[2]/button[1]')
        click_by_xpath(driver, '//*[@id="content"]/section/div/article/div[2]/div/div[5]/div[12]')
        sleep(45)
        driver.quit()

        # Get latest file
        file_path = get_latest_file()

        if file_path:
            # Install app
            install_app_by_cmd(file_path, "/S")
        else:
            print('Time out')
            return False

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error app: {e}')
        return False

import os
from time import sleep

from common_lib import check_program_installed, download_and_execute, \
    connect_app, download_by_link, click_by_xpath, print_all_windows, get_latest_file, run_file_exe, download_directory, \
    click_without_id, click_object, check_app_installed, check_app_installed_32, get_link


def QQ(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result
        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            # Download file
            driver = get_link(download_link)

            #Click Download
            click_by_xpath(driver, '//*[@id="cookie_action_close_header"]')
            sleep(5)
            click_by_xpath(driver, '//*[@id="cs-content"]/div[2]/div/div/div[4]/a')

            #Wait for download
            sleep(60)
            driver.quit()
            # Get latest file
            file_path = get_latest_file()

        # Run file exe
        run_file_exe(file_path)
        sleep(5)

        # Connect app
        target_window = connect_app('腾讯QQ安装向导')
        click_without_id(target_window, '阅读并同意', 'CheckBox')
        click_without_id(target_window, '立即安装', 'Button')
        sleep(20)
        click_without_id(target_window, '完成安装', 'Button')
        # Check app installed
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
result = QQ('QQ', 'QQ_9.9.17_250110_x64_01.exe', 'https://im.qq.com/pcqq/index.shtml')
print(result)
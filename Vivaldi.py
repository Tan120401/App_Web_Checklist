import os
from time import sleep

from common_lib import check_program_installed, download_and_execute, \
    connect_app, download_by_link, click_by_xpath, print_all_windows, get_latest_file, run_file_exe, download_directory, \
    click_without_id, click_object, check_app_installed, check_app_installed_32


def Vivaldi(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result
        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            # Download file
            driver = download_by_link(download_link)

            #Click Download
            click_by_xpath(driver, '//*[@id="section-desktop"]/div/div/div/div/a')

            #Wait for download
            sleep(35)
            # Get latest file
            file_path = get_latest_file()

        # Run file exe
        run_file_exe(file_path)
        sleep(5)

        #Connect app
        target_window = connect_app('Install Vivaldi')
        click_without_id(target_window, 'Accept and Install', 'Button')
        sleep(15)
        #Check app installed
        return True
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Vivaldi('Vivaldi', 'Vivaldi.7.1.3570.58.x64.exe', 'https://vivaldi.com')
print(result)
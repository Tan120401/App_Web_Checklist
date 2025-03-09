import os
from time import sleep
from common_lib import download_directory, connect_app, check_program_installed, \
    download_and_execute, print_all_windows, click_without_id, click_object, download_by_link, click_by_xpath, \
    get_latest_file, run_file_exe, install_app, get_link


def Goclean(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('°íÅ¬¸°')
        if result:
            return result

        # Check file install is existed
        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            # Download file
            driver = get_link(download_link)

            # Click Download
            click_by_xpath(driver, '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/div')

            # Wait for download
            sleep(10)
            # Get latest file
            file_path = get_latest_file()


        #Install app
        install_app(file_path, "/S")

        # Check app installed
        for i in range(24):
            result = check_program_installed('°íÅ¬¸°')
            if result:
                return result
            sleep(5)
    except Exception as e:
        print(f'error app: {e}')
        return False


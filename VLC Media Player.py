import os
from time import sleep

from common_lib import check_program_installed, download_and_execute, \
    connect_app, download_by_link, click_by_xpath, print_all_windows, get_latest_file, run_file_exe, download_directory, \
    click_without_id, click_object

def VLC_Media_Player(app_name, file_name_exe, download_link):
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
            click_by_xpath(driver, '//*[@id="downloadButton2"]')
            #Wait for download
            sleep(20)
            # Get latest file
            file_path = get_latest_file()

        # Run file exe
        run_file_exe(file_path)
        sleep(5)

        #Select language
        select_language_window = connect_app('Installer Language')
        click_without_id(select_language_window, 'OK', 'Button')
        sleep(5)

        #Connect app
        target_window = connect_app('VLC media player Setup')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'Install', 'Button')
        #Wait for install
        sleep(20)
        click_without_id(target_window, 'Finish', 'Button')
        #Check app installed
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
result = VLC_Media_Player('VLC Media Player', 'vlc-3.0.21-win64.exe', 'https://www.videolan.org/vlc/')
print(result)
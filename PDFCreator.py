from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, connect_app, click_by_xpath, \
    get_latest_file, click_without_id, click_object, close_app

def PDFCreator(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download file
        driver = download_by_link(download_link)
        sleep(5)

        #Click download
        click_cookies = click_by_xpath(driver, '//*[@id="gdpr-cc-btn-accept"]')
        if not click_cookies:
            click_center = click_by_xpath(driver, '//*[@id="mainContent"]/div/div/div/div[2]/div/div/div/div[1]/div/a')
            sleep(5)
            click_cookies = click_by_xpath(driver, '//*[@id="gdpr-cc-btn-accept"]')
        click_by_xpath(driver, '//*[@id="mainContent"]/div/div/div/div[2]/div/div/div/div[1]/div/a')
        sleep(15)

        # Get latest file
        latest_file = get_latest_file()

        # Run file exe
        run_file_exe(latest_file)
        sleep(8)
        # Connect app
        target_window = connect_app('PDFCreator')
        click_without_id(target_window, '_Install', 'Text')
        #Wait for install
        sleep(30)
        close_app(app_name)
        target_popup = connect_app('PDF Architect 9 Installer')
        click_object(target_popup, 'No', '7','Button')
        #Check installation
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False



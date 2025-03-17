import os

from time import sleep

from common_lib import download_by_link, check_program_installed, download_and_execute, connect_app, \
    click_by_xpath, get_latest_file, run_file_exe, click_without_id, get_link


def GOOSE_GOOSE_DUCK(app_name, file_name_exe, link):
    try:
        #Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        #Download and execute install file
        driver = get_link(link)

        sleep(10)

        #Click download
        click_by_xpath(driver, '/html/body/app-root/div/div/app-goose-goose-duck/app-ggd-main/section[2]/div/div/div/div/div[3]/div[1]/div[1]/a')
        sleep(150)
        driver.quit()

        #Get latest file
        latest_file = get_latest_file()
        #Run file exe
        run_file_exe(latest_file)

        # Connect app
        target_window = connect_app('Setup - Goose Goose Duck')
        click_without_id(target_window, 'I accept the agreement', 'RadioButton')
        click_without_id(target_window, 'Next', 'Button')
        click_without_id(target_window, 'Next', 'Button')
        click_without_id(target_window, 'Next', 'Button')
        click_without_id(target_window, 'Next', 'Button')
        click_without_id(target_window, 'Install', 'Button')
        click_without_id(target_window, 'Next', 'Button')
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

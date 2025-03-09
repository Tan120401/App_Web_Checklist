import os

from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_directory, \
    get_latest_file, connect_app, click_by_xpath, print_all_windows, click_without_id, close_app, get_link


def Alpdf(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('알PDF')
        if result:
            return result

        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            # Download file
            driver = get_link(download_link)
            click_by_xpath(driver, '//*[@id="container"]/section/div[1]/div/div[1]/div/div/div[1]/span/a')
            sleep(90)
            driver.quit()

            # Get latest file
            file_path = get_latest_file()

        # Run file exe
        run_file_exe(file_path)
        sleep(5)

        #Connect app
        target_window = connect_app('Setup - 알PDF')
        click_without_id(target_window,'Agree(A)', 'Button')
        sleep(10)
        almain_window = connect_app('알매니저')
        click_without_id(almain_window, '설치를 시작합니다.', 'Button')
        sleep(15)
        click_without_id(almain_window, '제품 실행', 'Button')
        click_without_id(almain_window, '동의 후 설치', 'Button')
        close_app('알PDF')
        click_without_id(almain_window, '취소', 'Button')
        close_app('알매니저')

        # Check app installed
        for i in range(24):
            result = check_program_installed('알PDF')
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Alpdf('Alpdf', 'ALPDF403.exe', 'https://altools.co.kr/product/ALPDF')
print(result)
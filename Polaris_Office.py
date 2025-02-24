import os
from time import sleep

from common_lib import download_by_link, run_file_exe, click_by_xpath

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'PolarisOfficeSetup.exe')

if not os.path.isfile(file_path):
    driver = download_by_link('https://www.polarisoffice.com/en/download')
    sleep(10)

    click_by_xpath(driver, '//*[@id="personal"]/div[1]/div[2]/div[1]/div/div/a[1]')

    sleep(90)

run_file_exe(file_path)

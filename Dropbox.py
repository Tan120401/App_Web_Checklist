import os
from time import sleep

from common_lib import download_by_link, get_download_folder, run_file_exe, click_by_xpath

# Lấy thông tin thư mục tải xuống mặc định
download_directory = get_download_folder()

# Đường dẫn đến tệp thực thi GOMAUDIOGLOBALSETUP_NEW.EXE
file_path = os.path.join(download_directory, 'DropboxInstaller.exe')

if not os.path.isfile(file_path):
    driver = download_by_link('https://www.dropbox.com/install')
    sleep(30)

    # Click Decline
    # click_by_xpath(driver, '//*[@id="decline_cookies_button"]/span')
    # sleep(5)

    #Click install
    click_by_xpath(driver, '//*[@id="component2400689423595428325"]/div/div/main/div/a')
    sleep(5)
    # // *[ @ id = "accept_all_cookies_button"] / span
    #Click skip
    click_by_xpath(driver, '/html/body/div[10]/div/div/div/div/div[1]/div[2]/div')
    sleep(5)

#Run file exe nếu đã có
run_file_exe(file_path)
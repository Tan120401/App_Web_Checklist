import os
import platform
import subprocess
from time import sleep

from common_lib import download_by_link, get_download_folder, run_file_exe, click_by_xpath

# Lấy thông tin thư mục tải xuống mặc định
download_directory = get_download_folder()

# Đường dẫn đến tệp thực thi GOMAUDIOGLOBALSETUP_NEW.EXE
file_path = os.path.join(download_directory, 'MelonSetup.exe')

if not os.path.isfile(file_path):
    driver = download_by_link('https://www.melon.com/customer/serviceintro/index.htm')
    sleep(10)
    click_by_xpath(driver, '//*[@id="conts"]/section[1]/div[1]/button[1]')
    sleep(20)


#Run file exe nếu đã có
run_file_exe(file_path)
import os
import platform
import subprocess
from time import sleep

from common_lib import download_by_link, get_download_folder, run_file_exe, click_by_xpath

# Lấy thông tin thư mục tải xuống mặc định
download_directory = get_download_folder()

# Đường dẫn đến tệp thực thi GOMAUDIOGLOBALSETUP_NEW.EXE
file_path = os.path.join(download_directory, 'Creative_Cloud_Set-Up.exe')

if not os.path.isfile(file_path):
    driver = download_by_link('https://creativecloud.adobe.com/apps/download/creative-cloud')
    sleep(10)
    click_by_xpath(driver, '//*[@id="cc-download-page"]/section[1]/div[1]/button[1]')
    sleep(20)

#Run file exe nếu đã có
run_file_exe(file_path)
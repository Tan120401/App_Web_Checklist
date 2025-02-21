import os
from time import sleep

from common_lib import download_by_link, get_download_folder, run_file_exe

# Lấy thông tin thư mục tải xuống mặc định
download_directory = get_download_folder()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'STOVESetup.exe')

if not os.path.isfile(file_path):
    download_by_link('https://dl-dev.onstove.com/temp/STOVESetup.exe')
    sleep(10)

run_file_exe(file_path)

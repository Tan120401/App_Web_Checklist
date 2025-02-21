import os
from time import sleep

from common_lib import download_by_link, get_download_folder, run_file_exe

# Lấy thông tin thư mục tải xuống mặc định
download_directory = get_download_folder()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'world_of_tanks_install_asia_d7xwpwyusv1x.exe')

if not os.path.isfile(file_path):
    download_by_link('https://redirect.wargaming.net/WoT/latest_web_install_asia')
    sleep(120)

run_file_exe(file_path)



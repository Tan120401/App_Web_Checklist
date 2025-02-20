import os
import platform
import subprocess
from time import sleep

from common_lib import download_by_link, get_download_folder, run_file_exe

# Lấy thông tin thư mục tải xuống mặc định
download_directory = get_download_folder()

# Đường dẫn đến tệp thực thi GOMAUDIOGLOBALSETUP_NEW.EXE
file_path = os.path.join(download_directory, 'ALSong352.exe')

if not os.path.isfile(file_path):
    download_by_link('https://advert.estsoft.com/?event=200803271705239')
    sleep(20)

#Run file exe nếu đã có
run_file_exe(file_path)
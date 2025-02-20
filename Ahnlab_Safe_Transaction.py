import os
import platform
import subprocess
from time import sleep

from common_lib import download_by_link, get_download_folder

# Lấy thông tin thư mục tải xuống mặc định
download_directory = get_download_folder()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'GOMAUDIOGLOBALSETUP_NEW.EXE')

if not os.path.isfile(file_path):
    download_by_link('https://cdn2.gomlab.com/gretech/audio/GOMAUDIOGLOBALSETUP_NEW.EXE')
    sleep(20)

# Kiểm tra lại xem tệp đã tồn tại chưa
if os.path.isfile(file_path):
    print('Tệp đã được tải xuống. Đang chạy tệp...')
    if platform.system() == "Windows":
        subprocess.run([file_path], shell=True)
    elif platform.system() == "Darwin":
        subprocess.run(["open", file_path])
    else:
        subprocess.run(["xdg-open", file_path])
else:
    print('Tệp chưa được tải xuống thành công.')
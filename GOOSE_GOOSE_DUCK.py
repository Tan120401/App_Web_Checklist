import os
import platform
import subprocess
from time import sleep

from common_lib import download_by_link, get_download_folder, run_file_exe

# Lấy thông tin thư mục tải xuống mặc định
download_directory = get_download_folder()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'Goose Goose Duck Installer 3.14.01 release.exe')

if not os.path.isfile(file_path):
    download_by_link('https://firebasestorage.googleapis.com/v0/b/gaggle-staging.appspot.com/o/Builds%2FGGD%2FGoose%20Goose%20Duck%20Installer%203.14.01%20release.exe?alt=media&token=064327c1-bffe-472e-ad46-30ebb0fa4978')
    sleep(10)

run_file_exe(file_path)
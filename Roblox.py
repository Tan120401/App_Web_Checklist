import os
from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'RobloxPlayerInstaller.exe')

if not os.path.isfile(file_path):
    download_by_link('https://www.roblox.com/download/client?os=win')
    sleep(20)

run_file_exe(file_path)

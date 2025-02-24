import os

from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'EAappInstaller.exe')

if not os.path.isfile(file_path):
    download_by_link('https://origin-a.akamaihd.net/EA-Desktop-Client-Download/installer-releases/EAappInstaller.exe')
    sleep(10)

run_file_exe(file_path)
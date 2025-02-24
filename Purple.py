import os
from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'PurpleInstaller_2_25_212_6.exe')

if not os.path.isfile(file_path):
    download_by_link('https://gs-purple-inst.download.ncupdate.com/Purple/PurpleInstaller_2_25_212_6.exe')
    sleep(90)

run_file_exe(file_path)

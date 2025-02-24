import os

from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'BANDIZIP-SETUP-STD-X64.EXE')

if not os.path.isfile(file_path):
    download_by_link('/bandizip/dl.php?web')
    sleep(10)

run_file_exe(file_path)

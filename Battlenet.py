import os
from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'Battle.net-Setup.exe')

if not os.path.isfile(file_path):
    download_by_link('https://www.blizzard.com/download/confirmation?product=bnetdesk')
    sleep(10)

run_file_exe(file_path)
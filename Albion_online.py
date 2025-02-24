import os
from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'albion-online-setup.exe')

if not os.path.isfile(file_path):
    download_by_link('//live.albiononline.com/clients/20250214110215/albion-online-setup.exe')
    sleep(30)

run_file_exe(file_path)

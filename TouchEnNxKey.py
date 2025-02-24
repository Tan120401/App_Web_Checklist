import os

from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'TouchEn_nxKey_32bit.exe')

if not os.path.isfile(file_path):
    download_by_link('https://bank.shinhan.com/sw/initech/extension/down/INIS_EX_SHA2.exe?ver=1.0.1.961')
    sleep(10)

run_file_exe(file_path)
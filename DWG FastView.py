import os

from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'DWGFastView(KR-1)_x64_1.exe')

if not os.path.isfile(file_path):
    download_by_link('https://advert.estsoft.com/?event=201110311523647')
    sleep(20)

run_file_exe(file_path)

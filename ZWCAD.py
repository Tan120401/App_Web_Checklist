import os
from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'ZWCAD2025설치및활성화(Standalone).pdf')

if not os.path.isfile(file_path):
    download_by_link('https://www.zwsoft.co.kr/download/download_simple.asp?fileNm=ZWCAD2025%EC%84%A4%EC%B9%98%EB%B0%8F%ED%99%9C%EC%84%B1%ED%99%94(Standalone).pdf&downNm=Menu_DOWN_LIST_Str_20240531_113907_2')
    sleep(10)

run_file_exe(file_path)


import os

from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'readerdc64_ga_cra_install.exe')

if not os.path.isfile(file_path):
    download_by_link('https://admdownload.adobe.com/rdcm/installers/live/readerdc64_ga_cra_install.exe')
    sleep(10)

run_file_exe(file_path)

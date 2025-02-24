import os

from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'pdfelement-pro_setup_full5239.exe')

if not os.path.isfile(file_path):
    download_by_link('https://download.wondershare.com/pdfelement-pro_full5239.exe?_gl=1*15dl66l*_ga*OTQ2NTk5MDE3LjE3NDAzNjE2MzQ.*_ga_24WTSJBD5B*MTc0MDM2MTYzMy4xLjAuMTc0MDM2MTYzNS42MC4wLjE2NDIwNDk4NQ..*_gcl_au*MTc0MTcxMjM3MC4xNzQwMzYxNjM2')
    sleep(10)

run_file_exe(file_path)

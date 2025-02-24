import os
from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'Blitz-2.1.263.exe')

if not os.path.isfile(file_path):
    download_by_link('https://sg-public-api.hoyoverse.com/event/download_porter/trace/ys_global/genshinimpactpc/default?url=https%3A%2F%2Fgenshin.hoyoverse.com%2Fko%2Fhome&appid=525')
    sleep(30)

run_file_exe(file_path)

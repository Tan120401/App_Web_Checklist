import os

from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi GOMAUDIOGLOBALSETUP_NEW.EXE
file_path = os.path.join(download_directory, 'ALSong352.exe')

if not os.path.isfile(file_path):
    download_by_link('https://advert.estsoft.com/?event=200803271705239')
    sleep(20)

#Run file exe nếu đã có
run_file_exe(file_path)
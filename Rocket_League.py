import os
from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'RobloxPlayerInstaller.exe')

if not os.path.isfile(file_path):
    download_by_link('https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi?trackingId=eca5b106b4b549959b4d27c8f3d03924')
    sleep(20)
run_file_exe(file_path)



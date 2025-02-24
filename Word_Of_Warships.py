import os
from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'world_of_warships_ww_install_asia_d7xwxhtjontu.exe')

if not os.path.isfile(file_path):
    download_by_link('https://wds.wargaming.net/wgc/releases_tTrHgLCKHBRiaL/wgc_24.08.02.8277_asia/world_of_warships_ww_install_asia.exe?sid=SIDHqNAIQCeD_VPqE14lFlbFSTvTeDty7bOXWfcS-MJAsFvu_d8W7m-if8zOjqqofNxS14iJ2Kmy6OUV1qmlgfZXVmajwBtkVJAoP2GXHJ4gsYiqfX2POOtRNfIWHcHO662ZZoNqFJa3d_Ylg&enctid=d7xwxhtjontu&lpsn=WoWs+direct+WGC+download+ASIA&foris=1&teclient=1740119043985793231&utm_source=wg_web_site&utm_medium=organic&utm_campaign=y3dwj24l&utm_content=unknown')
    sleep(10)

run_file_exe(file_path)





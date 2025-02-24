import os
from time import sleep

from pywinauto import Desktop

from common_lib import download_by_link, run_file_exe, download_directory, connect_app


def Alcapture():
    try:
        # Đường dẫn đến tệp thực thi
        file_path = os.path.join(download_directory, 'ALPDF403.exe')

        if not os.path.isfile(file_path):
            download_by_link('https://advert.estsoft.com/?event=201110311523647')
            sleep(10)

        run_file_exe(file_path)
        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Setup - 알PDF 4.03')
        #
        all_window = Desktop(backend='win32').windows()
        for win in all_window:
            print(win.window_text())
        print(target_window.print_control_identifiers())

        return True
    except Exception as e:
        print(f'error app: {e}')
        return False

Alcapture()
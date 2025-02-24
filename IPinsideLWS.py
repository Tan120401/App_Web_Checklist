import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, check_program_installed


def IPinsideLWS():
    try:
        result = check_program_installed('IPinside LWS Agent')
        if result:
            return result
        # Đường dẫn đến tệp thực thi
        file_path = os.path.join(download_directory, 'I3GSvcManager.exe')

        if not os.path.isfile(file_path):
            download_by_link('https://mybank.ibk.co.kr/IBK/uib/sw/interezen/agent/I3GSvcManager.exe')
            sleep(10)

        # Hàm kiểm tra xem nếu đã tồn tại file cài đặt thì run nó
        run_file_exe(file_path)
        sleep(10)
        # Kết nối tới màn hình cài đặt app
        # target_window = connect_app('APS Engine')
        #
        # #Click next
        # click_object(target_window, '´ÙÀ½ >', '1', 'Button')
        #
        # # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed('IPinside LWS Agent')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
IPinsideLWS()
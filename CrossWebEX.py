import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, connect_app, click_object, \
    check_program_installed


def CrossWebEX():
    try:
        result = check_program_installed('CrossWeb EX V3')
        if result:
            return result
        # Đường dẫn đến tệp thực thi
        file_path = os.path.join(download_directory, 'INIS_EX_SHA2.exe')

        if not os.path.isfile(file_path):
            download_by_link('https://bank.shinhan.com/sw/initech/extension/down/INIS_EX_SHA2.exe?ver=1.0.1.961')
            sleep(10)

        # Hàm kiểm tra xem nếu đã tồn tại file cài đặt thì run nó
        run_file_exe(file_path)
        sleep(10)
        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('CrossWeb EX')

        #Click close
        click_object(target_window, 'Close', '', 'Button')

        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed('CrossWeb EX V3')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

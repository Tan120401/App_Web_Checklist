import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, connect_app, print_all_windows, click_object, \
    check_program_installed, click_without_id


def Wizin_Delfino_G3():
    try:
        result = check_program_installed('Delfino G3')
        if result:
            return result
        # Đường dẫn đến tệp thực thi
        file_path = os.path.join(download_directory, 'delfino-g3-sha2.exe')

        if not os.path.isfile(file_path):
            download_by_link('https://mybank.ibk.co.kr/IBK/uib/sw/wizvera/delfino/down/delfino-g3-sha2.exe')
            sleep(10)

        # Hàm kiểm tra xem nếu đã tồn tại file cài đặt thì run nó
        run_file_exe(file_path)
        sleep(3)
        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Delfino G3')

        #Click next
        # click_object(target_window, 'Next >', '6489300', 'Button')
        click_without_id(target_window, 'Next >', 'Button')
        sleep(10)
        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed('Delfino G3')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

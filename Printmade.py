import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, check_program_installed, print_all_windows


def Printmade():
    try:
        result = check_program_installed('Printmade')
        if result:
            return result
        # Đường dẫn đến tệp thực thi
        file_path = os.path.join(download_directory, 'Printmade3_setup.exe')

        if not os.path.isfile(file_path):
            download_by_link('https://bank.shinhan.com/sw/printmade/download_files/Windows/Printmade3_setup.exe')
            sleep(10)

        # Hàm kiểm tra xem nếu đã tồn tại file cài đặt thì run nó
        run_file_exe(file_path)
        sleep(2)
        print_all_windows()
        # Kết nối tới màn hình cài đặt app
        # target_window = connect_app('APS Engine')
        #
        # #Click next
        # click_object(target_window, '´ÙÀ½ >', '1', 'Button')
        #
        # # Kiem tra xem da cai dat thanh cong hay chua
        # result = check_program_installed('APS Engine')
        # return result
    except Exception as e:
        print(f'error install: {e}')
        return False

Printmade()
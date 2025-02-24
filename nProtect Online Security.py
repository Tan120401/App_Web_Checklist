import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_directory, check_program_installed, print_all_windows, \
    connect_app, click_object

def nProtect_Online_Security():
    try:
        result = check_program_installed('nProtect Online Security')
        if result:
            return result
        # Đường dẫn đến tệp thực thi
        file_path = os.path.join(download_directory, 'nos_setup.exe')

        if not os.path.isfile(file_path):
            download_by_link('https://supdate.nprotect.net/nprotect/nos_service/windows/install/nos_setup.exe')
            sleep(10)

        # Hàm kiểm tra xem nếu đã tồn tại file cài đặt thì run nó
        run_file_exe(file_path)
        sleep(2)
        print_all_windows()
        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('nProtect Online Security')

        #Click install
        click_object(target_window, 'Install', '1', 'Button')
        sleep(12)
        # # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed('nProtect Online Security')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

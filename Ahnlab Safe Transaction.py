

from common_lib import download_by_link, run_file_exe, download_directory, connect_app, \
    click_object, check_program_installed


def Ahnlab_Safe_Transaction():
    try:
        # Đường dẫn đến tệp thực thi
        file_path = os.path.join(download_directory, 'astxdn.exe')

        # Kiểm tra đã có file cài đặt chưa, nếu chưa thực hiện tải xuống
        if not os.path.isfile(file_path):
            download_by_link('https://bank.shinhan.com/sw/astx/astxdn.exe')
            sleep(10)

        # Hàm kiểm tra xem nếu đã tồn tại file cài đặt thì run nó
        run_file_exe(file_path)
        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('AhnLab Safe Transaction Setup')

        #Click next
        click_object(target_window, 'Next >', '1', 'Button')
        #Click i agree
        click_object(target_window, 'I Agree', '1', 'Button')
        # Click finished
        click_object(target_window, 'Finished', '1', 'Button')
        sleep(60)
        result = check_program_installed('AhnLab Safe Transaction')
        return result
    except Exception as e:
        print(f'App handle error: {e}')
        return  False




from common_lib import download_by_link, run_file_exe, download_and_execute, check_program_installed, connect_app, \
    click_object, click_object_by_index, click_without_id


def Bandizip(app_name, file_name_exe, download_link):
    try:

        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 30, 10)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Install Bandizip')
        click_object_by_index(target_window, '', 'Pane', 1)
        print(target_window.print_control_identifiers())
        click_without_id(target_window, 'Agree and Install', 'Pane')
        sleep(5)
        click_without_id(target_window, 'Close', 'Pane')

        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
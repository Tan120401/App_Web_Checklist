from common_lib import download_and_execute, check_program_installed, connect_app, click_without_id


def Alsong(app_name, file_name_exe, download_link):
    try:

        # Check app is installed
        result = check_program_installed('알송')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 20, 5)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Setup')
        #Click Agree
        click_without_id(target_window, 'Agree(A)', 'Button')
        print(target_window.print_control_identifiers())

        result = check_program_installed('알송')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

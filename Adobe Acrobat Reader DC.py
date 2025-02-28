from common_lib import download_and_execute, connect_app, click_object, check_program_installed

def Adobe_Acrobat_Reader(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 30, 120)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Adobe Acrobat Reader Installer')
        # Click finished
        click_object(target_window, 'Finish', 'primary-button', 'Button')
        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed('Adobe Acrobat')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

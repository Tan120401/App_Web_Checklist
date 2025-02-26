from common_lib import  connect_app, \
    click_object, check_program_installed, download_and_execute

def APS_Engine(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 20, 10)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('APS Engine')

        # Click next
        click_object(target_window, '´ÙÀ½ >', '1', 'Button')
        click_object(target_window, 'À§ »çÇ×¿¡ µ¿ÀÇÇÕ´Ï´Ù.', '1034', 'CheckBox')
        click_object(target_window, '¼³Ä¡', '1', 'Button')
        click_object(target_window, '¸¶Ä§', '1', 'Button')

        # Kiem tra xem da cai dat thanh cong hay chua
        result = check_program_installed('APS Engine')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
from time import sleep

from common_lib import download_and_execute, connect_app, click_object, check_program_installed, click_without_id


def Adobe_Acrobat_Reader(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('Adobe Acrobat')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Adobe Acrobat Reader Installer')


        # Check app installed
        for i in range(36):
            result = check_program_installed('Adobe Acrobat')
            finished = click_without_id(target_window, 'Finish', 'Button')
            if result and finished[0]:
                return result
            sleep(10)
        return True
    except Exception as e:
        print(f'error install: {e}')
        return False

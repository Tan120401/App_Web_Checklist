from time import sleep

from common_lib import check_program_installed, download_exe_file, install_app_by_cmd


def Tom_Clancy_Rainbow_Six_Siege(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('Ubisoft Connect')
        if result:
            return result

        # Download file
        file_path = download_exe_file(file_name_exe, download_link)
        if file_path:
            # Install app
            install_app_by_cmd(file_path, "/S")
        else:
            print('Time out')
            return False

        # Check app installed
        for i in range(24):
            result = check_program_installed('Ubisoft Connect')
            print('dang check')
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error app: {e}')
        return False

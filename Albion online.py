from time import sleep

from common_lib import download_and_execute, print_all_windows, connect_app, \
    click_object, check_program_installed, download_exe_file, install_app

def Albion_online(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download file
        file_path = download_exe_file(file_name_exe, download_link)
        if file_path:
            # Install app
            install_app(file_path, "/S")
        else:
            print('Time out')
            return False

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

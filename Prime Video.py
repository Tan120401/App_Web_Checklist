from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app

def Prime_Video(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 5, 5)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('Microsoft Store')
        click_without_id(target_window, 'Install', 'Button')
        sleep(40)
        close_app('Prime Video for Windows')
        # Check app install
        return True
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Prime_Video('Prime Video', 'Prime Video for Windows Installer.exe', 'https://get.microsoft.com/installer/download/9P6RC76MSMMJ?hl=en-us&gl=en&referrer=storeforweb&ocid=sfw-fab-control')
print(result)

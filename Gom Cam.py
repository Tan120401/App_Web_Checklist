from time import sleep
from common_lib import download_directory, connect_app, check_program_installed, \
    download_and_execute, print_all_windows, click_without_id, click_object

def Gom_Cam(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('Installer Language')
        click_object(target_window, 'OK', '1', 'Button')
        sleep(5)

        gom_window = connect_app('GOM Cam Setup')
        click_object(gom_window, 'Next >', '1', 'Button')
        click_object(gom_window, 'I Agree', '1', 'Button')
        click_object(gom_window, 'Next >', '1', 'Button')
        click_object(gom_window, 'Install', '1', 'Button')
        sleep(15)
        click_object(gom_window, 'Finish', '1', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed('알캡처')
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error app: {e}')
        return False

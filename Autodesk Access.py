from time import sleep

from common_lib import download_and_execute, connect_app, check_program_installed, \
    print_all_windows, click_without_id

def Autodesk_Access(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 30, 30)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('Autodesk Access Installer')
        click_without_id(target_window, 'I agree to the Terms of Use', 'CheckBox')
        click_without_id(target_window, 'Install', 'Button')
        #Wait for installation
        sleep(30)
        #Check installation
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

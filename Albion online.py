from time import sleep

from common_lib import download_and_execute, print_all_windows, connect_app, \
    click_object, check_program_installed

def Albion_online(app_name, file_name_exe, download_link):
    try:
        #Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        #Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 20, 10)

        #If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('Albion Online Setup')
        #Click next
        click_object(target_window, 'Next >', '1', 'Button')
        click_object(target_window, 'OK', '2', 'Button')
        click_object(target_window, 'Next >', '1', 'Button')
        click_object(target_window, 'Install', '1', 'Button')

        # wait install
        sleep(10)
        click_object(target_window, 'Close', '1', 'Button')

        #Check app is installed
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

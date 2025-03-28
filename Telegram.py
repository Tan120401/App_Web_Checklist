from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app, check_app_installed, \
    check_app_installed_32


def Telegram(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 3)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        #Select language
        language_window = connect_app('Select Setup Language')
        click_without_id(language_window, 'OK', 'Button')
        sleep(2)

        #Connect app
        target_window = connect_app('Setup - Telegram Desktop')
        click_without_id(target_window,'Next', 'Button')
        click_without_id(target_window,'Next', 'Button')
        click_without_id(target_window,'Next', 'Button')
        click_without_id(target_window,'Install', 'Button')
        sleep(20)
        click_without_id(target_window,'Finish', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

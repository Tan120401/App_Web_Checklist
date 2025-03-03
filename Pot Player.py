from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app

def PotPlayer(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 12, 5)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        # Select language
        select_language_window = connect_app('Installer Language')
        click_without_id(select_language_window, 'OK', 'Button')
        sleep(5)

        # Connect app
        target_window = connect_app('PotPlayer-64')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'I Agree', 'Button')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'Install',  'Button')
        sleep(15)
        click_object(target_window, 'Close', '1', 'Button')

        sleep(5)
        codec_window = connect_app('Open Codec for PotPlayer Setup')
        # click_without_id(codec_window, 'Cancel', 'Button')
        click_without_id(codec_window, 'Yes', 'Button')
        # Check app install
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False

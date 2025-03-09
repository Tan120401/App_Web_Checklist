from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app

def BANDIVIEW(app_name, file_name_exe, download_link):
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
        target_window = connect_app('Install BandiView')
        click_object_by_index(target_window, '', 'Pane', 1)
        click_without_id(target_window, 'Agree and Install', 'Pane')
        click_without_id(target_window, 'Close', 'Pane')
        sleep(10)

        setup_window = connect_app('Associate file extensions to BandiView')
        click_object(setup_window, 'OK', '1', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

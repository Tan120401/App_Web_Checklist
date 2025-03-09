from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    click_object, click_without_id

def Rocket_League(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('Epic Games Launcher')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('Epic Games Launcher Setup')
        click_without_id(target_window, 'Install', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed('Epic Games Launcher')
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False
from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    click_without_id

def World_of_Warships(app_name, file_name_exe, download_link):
    try:
        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 5)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result
        # Connect app
        target_window = connect_app('Wargaming.net Game Center')
        # #click accept and install
        click_without_id(target_window, 'INSTALL', 'Text')

        # Check app installed
        for i in range(36):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False



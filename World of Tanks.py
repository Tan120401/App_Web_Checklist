from time import sleep

from common_lib import check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_without_id

def World_of_Tanks(app_name, file_name_exe, download_link):
    try:
        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10, 5)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result
        # Connect app
        target_window = connect_app('Wargaming.net Game Center')
        #click accept and install
        click_without_id(target_window, 'ACCEPT & INSTALL', 'Text')
        #Click next
        sleep(20)
        #Wait for installation
        return True
    except Exception as e:
        print(f'error install: {e}')
        return False

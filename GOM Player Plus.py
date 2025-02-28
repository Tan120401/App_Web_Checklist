from time import sleep
from common_lib import download_directory, connect_app, check_program_installed, \
    download_and_execute, print_all_windows, click_without_id, click_object


def GOM_Player_Plus(app_name, file_name_exe, download_link):
    try:
        # # Check app is installed
        # result = check_program_installed(app_name)
        # if result:
        #     return result
        #
        # # Download and execute install file
        # download_result = download_and_execute(file_name_exe, download_link, 20, 10)
        #
        # # If download and execute fail -> return fail
        # if not download_result:
        #     return download_result
        #
        # # Connect app
        # target_window = connect_app('Installer Language')
        # click_object(target_window, 'OK', '1', 'Button')
        # sleep(5)

        setup_window = connect_app('GOM Player+')
        print(setup_window.print_control_identifiers())
        # Check app install
        result = check_program_installed('알캡처')

        return result
    except Exception as e:
        print(f'error app: {e}')
        return False
result = GOM_Player_Plus('GOM Player Plus', 'GOMPLAYERPLUS2024SETUP_NEW.EXE','https://cdn2.gomlab.com/gretech/gomplayerplus/GOMPLAYERPLUS2024SETUP_NEW.EXE')
print(result)
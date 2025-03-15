from time import sleep

from common_lib import download_and_execute, connect_app, print_all_windows, check_app_existed, click_without_id, \
    click_object_by_image, close_app

def Riot_Games(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_app_existed('Riot Client')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 8)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('League of Legends Installer')
        file_path_install = r'Resource/image/riot games/install.png'

        click_object_by_image(file_path_install, 0.8)


        # Check app installed
        for i in range(24):
            result = check_app_existed(app_name)
            if result:
                sleep(5)
                close_app('Riot Client')
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

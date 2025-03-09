from time import sleep

from common_lib import download_and_execute, connect_app, print_all_windows, check_app_existed, click_without_id, \
    click_object_by_image


def Riot_Games(app_name, file_name_exe, download_link):
    try:
        # # Check app is installed
        # result = check_app_existed('Riot Client')
        # if result:
        #     return result
        #
        # # Download and execute install file
        # download_result = download_and_execute(file_name_exe, download_link, 5)
        #
        # # If download and excute fail -> return fail
        # if not download_result:
        #     return download_result

        # Connect app
        target_window = connect_app('League of Legends Installer')
        file_path_install = r'Resource/image/riot games/install.png'
        click_object_by_image(file_path_install)


        # Check app installed
        for i in range(24):
            result = check_app_existed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Riot_Games('Riot Games', 'Install League of Legends sg2.exe', 'https://lol.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.sg2.exe')
print(result)

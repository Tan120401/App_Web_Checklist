from asyncio import set_event_loop_policy
from time import sleep

import pyautogui

from common_lib import check_program_installed, download_and_execute, connect_app, click_object_by_image, \
    check_app_installed, close_app


def Wondershare(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_app_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 5)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        #Connect app
        checkbox_file = r'Resource/image/checkbox.png'
        click_object_by_image(checkbox_file)

        next_file = r'Resource/image/filmora/next.png'
        click_object_by_image(next_file)

        #wait for install
        sleep(30)
        close_app('Wondershare Filmora')

        # Check app installed
        for i in range(24):
            result = check_app_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Wondershare('Wondershare', 'filmora_setup_full6119.exe', 'https://download.wondershare.kr/filmora_full6119.exe')
print(result)
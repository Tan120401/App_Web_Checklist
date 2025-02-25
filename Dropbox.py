
from time import sleep

from common_lib import download_and_execute, connect_app, check_program_installed


def Dropbox(app_name, file_name_exe, download_link):
    try:
        result = download_and_execute(app_name, file_name_exe, download_link, 30, 5)
        if result:
            return result
        # wait for install done
        sleep(90)
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
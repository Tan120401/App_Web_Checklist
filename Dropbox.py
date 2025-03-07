
from time import sleep

from common_lib import download_and_execute, connect_app, check_program_installed


def Dropbox(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 30, 5)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # wait for install done
        sleep(90)
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
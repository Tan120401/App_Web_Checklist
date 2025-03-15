from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, check_app_installed, check_app_existed, close_app


def Blitz(app_name, file_name_exe, download_link):
    try:
        #Check app is installed
        result = check_app_existed(app_name)
        if result:
            return result

        #Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10)

        #If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Check app installed
        for i in range(24):
            result = check_app_existed(app_name)
            if result:
                sleep(5)
                close_app('Launch Game ⚡ Blitz')
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

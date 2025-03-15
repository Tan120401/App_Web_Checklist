from time import sleep

from common_lib import download_by_link, run_file_exe, download_and_execute, check_program_installed, connect_app, \
    click_object


def Stove(app_name, file_name_exe, download_link):
    try:
        # # Check app is installed
        # result = check_program_installed(app_name)
        # if result:
        #     return result
        #
        # # Download and execute install file
        # download_result = download_and_execute(file_name_exe, download_link, 90)
        #
        # # If download and excute fail -> return fail
        # if not download_result:
        #     return download_result

        # Connect Stove
        target_window = connect_app('LauncherSetup')

        #Click next
        # print(target_window.print_control_identifiers())

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Stove('Stove', 'STOVESetup.exe', 'https://dl-dev.onstove.com/temp/STOVESetup.exe')
print(result)
from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app, check_app_installed


def Opera(app_name, file_name_exe, download_link):
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
        target_window = connect_app('Opera Installer')
        click_without_id(target_window, 'Accept and Install', 'Button')
        click_without_id(target_window, 'Accept', 'Button')

        # Check app installed
        for i in range(24):
            result = check_app_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Opera('Opera', 'OperaSetup.exe', 'https://www.opera.com/computer/thanks?ni=stable&os=windows')
print(result)
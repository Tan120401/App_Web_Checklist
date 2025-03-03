from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app, check_app_installed


def TeamViewer(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 20, 5)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        #Connect app
        target_window = connect_app('TeamViewer Setup')
        click_without_id(target_window,'Accept - next', 'Button')
        sleep(30)
        # Check app install
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
result = TeamViewer('TeamViewer', 'TeamViewer_Setup_x64.exe', 'https://dl.teamviewer.com/download/version_15x/TeamViewer_Setup_x64.exe?src=cookie-banner&ref=https%3A%2F%2Fwww.teamviewer.com%2Fvi%2F')
print(result)
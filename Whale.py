from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app

def Whale(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10, 5)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        #Conect app
        target_window = connect_app('NAVER Whale Installer')
        click_without_id(target_window, 'Accept and continue', 'Button')
        sleep(30)
        # Check app install
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Whale('Whale', 'WhaleSetup.exe', 'https://installer-whale.pstatic.net/downloads/installers/WhaleSetup.exe')
print(result)
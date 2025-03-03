from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app

def Kollus_Player(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 12, 5)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('Kollus Player')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'Install', 'Button')

        sleep(30)
        # Check app install
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Kollus_Player('Kollus Player', 'KollusAgent-3.1.1.1.r5.exe', 'https://v.kr.kollus.com/pc_player_install/agent?cpk=megastudyedu')
print(result)
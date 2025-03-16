import os

from time import sleep

from common_lib import download_by_link, run_file_exe, click_by_xpath, download_and_execute, connect_app, click_object, \
    check_program_installed, download_directory, click_without_id, close_app, print_all_windows, click_without_title


def Rockstar_Games_Launcher(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 5)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # # Kết nối tới màn hình cài đặt app
        target_window = connect_app('Rockstar Games Launcher Installer')
        click_without_title(target_window, '801', 'Button')
        click_without_title(target_window, '801', 'Button')
        click_without_id(target_window, "I accept Rockstar's Terms of Service", 'Image')
        click_without_title(target_window, '801', 'Button')
        click_without_title(target_window, '801', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                sleep(10)
                target_window.close()
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False

result = Rockstar_Games_Launcher('Rockstar Games Launcher', 'Rockstar-Games-Launcher.exe', 'https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe?_gl=1*tyd6fv*_gcl_au*MjQzNTIzNjk3LjE3NDIxMzM0Mjc.*_ga*MjM0NjIzMzA4LjE3NDIxMzM0MDU.*_ga_PJQ2JYZDQC*MTc0MjEzMzQwNC4xLjEuMTc0MjEzMzQ0MS4wLjAuMA..')
print(result)
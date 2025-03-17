from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app, check_app_installed, \
    check_app_installed_32, click_object_click_input


def MediBang_Paint_for_Pro(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 5)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        #Select language
        language_window = connect_app('Setup')
        click_without_id(language_window, 'Next', 'Button')
        sleep(5)

        #Connect app
        target_window = connect_app('MediBang Paint Pro Setup')
        click_without_id(target_window, 'Next', 'Button')
        sleep(20)
        click_without_id(target_window, 'Finish', 'Button')

        # Select language
        sleep(3)
        language_window = connect_app('Select Setup Language')
        click_without_id(language_window, 'OK', 'Button')

        # Check app install
        return True
    except Exception as e:
        print(f'error install: {e}')
        return False
result = MediBang_Paint_for_Pro('MediBang Paint for Pro', 'medibang-paint-pro-28.3-installer_3-jCp71.exe', 'https://en.softonic.com/download-launch?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb3dubG9hZFR5cGUiOiJyaXNlSW5zdGFsbGVyIiwiZG93bmxvYWRVcmwiOiJodHRwczovL2QxaGNrMzUxNzN6enBjLmNsb3VkZnJvbnQubmV0L2h1L3Vxc240anF2bXEvYWh5LzgxLjQ3MyIsImFwcElkIjoiNzk4MzhhYWMtZTI2MS00NTMwLThmN2YtOGNhMTUzNzEzNWZmIiwicGxhdGZvcm1JZCI6IndpbmRvd3MiLCJpYXQiOjE3NDIxNzYxODcsImV4cCI6MTc0MjE3OTc4N30.UnvpjzHs9S6xnSy9VYmxXmdAtWmWS2c9iJphUaiIMOc')
print(result)

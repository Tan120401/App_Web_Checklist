from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app, check_app_installed, \
    check_app_installed_32

def Vegas_Pro(app_name, file_name_exe, download_link):
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

        #Connect app
        target_window = connect_app('VEGAS Pro 22')
        click_without_id(target_window, ' Continue', 'Button')
        # Check app install
        sleep(30)
        return True
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Vegas_Pro('Vegas Pro', 'trial_vegaspro22_dlm_je96k4.exe', 'https://dl03.vegascreativesoftware.com/trial_vegaspro22_dlm_je96k4.exe')
print(result)

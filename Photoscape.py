from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app, check_app_installed, \
    check_app_installed_32

def Photoscape(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10, 5)

        # If download and execute fail -> return fail'
        if not download_result:
            return download_result

        #Connect app
        target_window = connect_app('PhotoScape')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'I Agree', 'Button')
        click_without_id(target_window, 'Next >', 'Button')
        click_without_id(target_window, 'Next >', 'Button')
        sleep(20)
        click_without_id(target_window, 'Finish', 'Button')

        # Check app install
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Photoscape('Photoscape', 'PhotoScape 3.4.exe', 'https://www.filehorse.com/download/file/sEqp0V5z8oWNsJ9_ZMWSa0uvz5zCCgScHGgKjT_TVv4Krm0BoXah6S7b5zDNxQIBIEg4qnkBxdjdSMC1ZGjR4Q/')
print(result)

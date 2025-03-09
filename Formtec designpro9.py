from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app, check_app_installed, \
    check_app_installed_32, click_object_click_input


def Formtec_designpro9(app_name, file_name_exe, download_link):
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

        #Connect app
        target_window = connect_app('Setup')
        click_without_id(target_window, 'Next', 'Button')
        click_without_id(target_window, 'Next', 'Button')
        click_without_id(target_window, 'Accept', 'Button')
        click_without_id(target_window, 'Accept', 'Button')
        sleep(30)
        click_without_id(target_window, 'Finish', 'Button')

        #Select language
        language_window = connect_app('Select Setup Language')
        click_without_id(language_window, 'OK', 'Button')
        target_window = connect_app('Setup')
        click_without_id(target_window, 'Yes', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Formtec_designpro9('Formtec designpro9', 'DesignPro_9_Setup_UP9.exe', 'https://download.formtec.co.kr/download/DesignPro_9_Setup_UP9.exe')
print(result)

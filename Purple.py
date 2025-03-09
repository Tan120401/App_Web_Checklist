from time import sleep

from common_lib import run_file_exe, download_and_execute, connect_app, check_program_installed, \
    click_object

def Purple(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('PURPLE Install')
        click_object(target_window, "Next >", "1", "Button")
        click_object(target_window, "I Agree", "1", "Button")
        click_object(target_window, "Install", "1", "Button")

        #Wait for install
        sleep(30)
        click_object(target_window, "Finish", "1", "Button")

        # Check app installed
        for i in range(24):
            result = check_program_installed(app_name)
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False


from time import sleep

from common_lib import check_program_installed, download_and_execute, connect_app, click_without_id

def Battlenet(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('Battle.net')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 30)

        # If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('Battle.net Setup')

        # #Click next
        click_without_id(target_window, 'Continue', 'Button')

        # Check app installed
        for i in range(24):
            result = check_program_installed('Battle.net')
            if result:
                return result
            sleep(10)
    except Exception as e:
        print(f'error install: {e}')
        return False


import os
from time import sleep
from common_lib import download_directory, connect_app, check_program_installed, \
    download_and_execute, print_all_windows, click_without_id, click_object, download_by_link, click_by_xpath, \
    get_latest_file, run_file_exe

def Turbo_Vaccine(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed('akazz')
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 10, 10)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result
        print_all_windows()
        # Connect app
        target_window = connect_app('¾Ë¾à ¼³Ä¡')

        # Check app install
        result = check_program_installed('a')
        if result:
            return result
    except Exception as e:
        print(f'error app: {e}')
        return False
result = Turbo_Vaccine('Turbo Vaccine','thiết_lập_Avast_Free_Antivirus_trực_tuyến.exe','https://www.turbovaccine.com/TVIS_R3_M.exe')
print(result)

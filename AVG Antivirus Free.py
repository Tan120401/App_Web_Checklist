import os
from time import sleep
from common_lib import download_directory, connect_app, check_program_installed, \
    download_and_execute, print_all_windows, click_without_id, click_object, download_by_link, click_by_xpath, \
    get_latest_file, run_file_exe, click_object_by_image


def AVG_Antivirus_Free(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        # Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 20, 10)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        install_path = r'Resource/image/avg antivirus/install.png'
        click_object_by_image(install_path)
        sleep(60)

        # Check app install
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error app: {e}')
        return False
result = AVG_Antivirus_Free('AVG Antivirus Free','avg_antivirus_free_setup.exe','https://www.avg.com/en-us/download-thank-you.php?product=FREEGSR-FAD#pc')
print(result)
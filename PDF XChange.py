import os
import zipfile
from time import sleep

from common_lib import download_and_execute, connect_app, click_object, check_program_installed, download_by_link, \
    get_latest_file, download_directory, run_file_exe, print_all_windows, click_without_id


def PDF_XChange(app_name, file_name_exe, download_link):
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result
        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            #Download file zip
            download_by_link(download_link)
            sleep(60)

            lastest_file_zip = get_latest_file()


            # Open ZIP
            with zipfile.ZipFile(lastest_file_zip, 'r') as zip_ref:
                # Extract all to Downloads
                zip_ref.extractall(download_directory)
            sleep(5)
            file_path = get_latest_file()

        run_file_exe(file_path)
        sleep(2)

        #Connect_app
        target_window = connect_app('PDF-XChange Editor Setup')
        click_object(target_window, 'Install', '1027', 'Button')
        sleep(5)
        click_object(target_window, 'Next', '1557', 'Button')
        click_object(target_window, 'I accept the terms in the License Agreement', '1635', 'CheckBox')
        click_object(target_window, 'Next', '1557', 'Button')
        click_object(target_window, 'CompleteIcon', '1648', 'Button')
        click_object(target_window, 'Next', '1557', 'Button')
        click_object(target_window, 'Install', '1586', 'Button')
        sleep(15)
        click_object(target_window, 'Finish', '1528', 'Button')
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
result = PDF_XChange('PDF-XChange Editor', 'PDFXVE10.exe',"https://www.pdf-xchange.de/DL/tracker10/editor-zip-tracker.php")
print(result)
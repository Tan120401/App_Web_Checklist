import subprocess
from time import sleep
from common_lib import *

#
app_name = 'PDF Architect'


def pdf_architect_9(app_name, file_name_exe, download_link):
    app_name = 'PDF Architect'
    try:
        # Check app is installed
        result = check_program_installed(app_name)
        if result:
            return
        # tao folder luu file tai ve
        download_directory = f'{get_download_folder()}\{app_name}'
        make_folder_log(download_directory)
        # Download and execute install file
        download_result = download_app(download_directory, download_link)

        # If download and execute fail -> return fail
        if not download_result:
            return download_result
        # Get a list of files in the folder
        file_names = os.listdir(download_directory)

        # Filter out .exe files
        install_files = [file for file in file_names if
                         (file.endswith('.exe') or file.endswith('.msi')) and os.path.isfile(
                             os.path.join(download_directory, file))]
        # Ensure download_directory and file_name_exe are correctly defined earlier in your code
        install_path = f"{download_directory}\{install_files[0]}"

        if '.exe' in install_files[0]:
            install_command = f'"{install_path}"'
        else:
            install_command = [
                "msiexec",
                "/i", install_path,  # /i for installation
                "/quiet",  # Silent install
                "/norestart"  # Prevent restart after installation
            ]
        # Install app with quoted paths
        print(install_command)
        install_app(install_command, 10)
        try:
            # Try to connect to the main window of PDF Architect
            app = Application(backend='uia').connect(title='PDF Architect')
            app_window = app['PDF Architect']
            if app_window.exists():
                app_window.set_focus()
                # Click the "NEXT" button in the main window
                next_button = app_window.child_window(title="NEXT", auto_id="Next", control_type="Button")
                next_button.click_input()

                # Try interacting with the trial window for a limited number of attempts
                for _ in range(60):
                    try:
                        # Try to connect to the trial window of PDF Architect
                        trial_window = app['PDF Architect - Trial']
                        if trial_window.exists():
                            trial_window.set_focus()
                            try_now_button = trial_window.child_window(title='Try Now')
                            if try_now_button.exists():
                                try_now_button.click_input()
                                sleep(1)
                                break

                        # Sleep and retry if not successful
                        sleep(10)

                        # Check if the app window is still present
                        app_window = app['PDF Architect']
                        if app_window:
                            app_window.print_control_identifiers()
                            app_window.set_focus()
                            close_button = app_window.child_window(auto_id='BtnClose')
                            if close_button.exists():
                                close_button.click_input()
                                sleep(1)
                                break
                    except Exception:
                        pass
                sleep(3)

        except Exception:
            pass
        sleep(5)


        # Check app install
        for i in range(6):
            result = check_app_existed(app_name)
            if result:
                print('cai dat thanh cong')
                return True
            sleep(10)

    except Exception as e:
        print(f'error install: {e}')
        return False

#
# if __name__ == '__main__':
#     download_link = 'https://www.pdfarchitect.org/download/?config=AF3CEDDA-7E46-429B-A312-C8F312C86063&amp;__hstc=113466648.8868cb281266d00566a6dc3d4b969c84.1741246812268.1741246812268.1741246812268.1&amp;__hssc=113466648.1.1741246812268&amp;__hsfp=2803957637?visitorId=e6865ff0-1a47-4b68-bdbf-f672170964c9&amp;culture=en&amp;referral=www.pdfforge.org%2Fpdfarchitect&amp;ref=pdfforge.org%2Fpdfarchitect&amp;wid=8193&amp;uid=1015225&amp;src=direct&amp;cmp=pdfa_all_o_all_all_all_architect&amp;key1=default&amp;key2=default&amp;keyb=none&amp;mkey1=pdfforge.org%2Fpdfarchitect&amp;mkey2=none&amp;mkey3=none&amp;mkey4=e6865ff0-1a47-4b68-bdbf-f672170964c9&amp;mkey5=none&amp;mkey6=039e4237-4cd2-4055-d20d-969f3dbf9796_2025-03-06&amp;mkey7=none&amp;mkey8=none&amp;mkey9=none&amp;mkey10=none&amp;gclid=none&amp;msclkid=none&amp;fbclid=none&amp;pixa=none&amp;partner=none&amp;qti=039e4237-4cd2-4055-d20d-969f3dbf9796_2025-03-06&amp;cid=1446315843.1741246812'
#     pdf_architect_9(app_name, 'PDFArchitectInstaller-p8hbqdpJ.exe', download_link)

    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

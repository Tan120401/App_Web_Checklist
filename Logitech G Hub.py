import subprocess
from time import sleep
from common_lib import *

app_name = 'Logitech G'


def Logitech_G_Hub(app_name, file_name_exe, download_link):
    app_name = 'Logitech G'
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
            install_command = f'"{install_path}" --silent'
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

        # Check app install
        for i in range(60):
            try:
                app = Application(backend='uia').connect(title='Logitech G HUB')
                app_window = app['Logitech G HUB']
                if app_window:
                    app_window.set_focus()
                close_btn = app_window.child_window(title="Close", control_type="Image")
                if close_btn:
                    close_btn.invoke()
                    sleep(1)
            except Exception as e:
                pass
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
#     download_link = 'https://www.libreoffice.org/donate/dl/win-x86_64/25.2.1/ko/LibreOffice_25.2.1_Win_x86-64.msi'
#     Logitech_G_Hub(app_name, 'LibreOffice_25.2.1_Win_x86-64.msi', download_link)

    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

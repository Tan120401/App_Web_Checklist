import subprocess
from time import sleep
from common_lib import *

#
app_name = '네이버 eBook 리더'


def Naver_eBook_Reader(app_name, file_name_exe, download_link):
    app_name = '네이버 eBook 리더'
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
            install_command = f'"{install_path}" /S'
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
        for i in range(60):
            try:
                # # Connect to the application using the 'win32' backend
                app = Application(backend='uia').connect(title='Information')
                information_window = app['Information']
                if information_window.exists():
                    information_window.set_focus()
                    sleep(1)
                    information_window.child_window(title='Yes').click_input()
                    sleep(5)
            except Exception as e:
                pass
            sleep(1)
        for i in range(30):
            try:
                # # Connect to the application using the 'win32' backend
                app = Application(backend='uia').connect(title='Information')
                information_window = app['Information']
                if information_window.exists():
                    information_window.set_focus()
                    sleep(1)
                    information_window.child_window(title='No').click_input()
                    sleep(2)
            except Exception as e:
                pass
            sleep(1)
        # # Check app install
        # for i in range(60):
        #     result = check_app_existed(app_name)
        #     if result:
        #         print('cai dat thanh cong')
        #         return True
        #     sleep(10)

    except Exception as e:
        print(f'error install: {e}')
        return False
    return True

# if __name__ == '__main__':
#     download_link = 'https://appdown.pstatic.net/naver/pcebookviewer/NBInstaller.exe'
#     Naver_eBook_Reader(app_name, '', download_link)

    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

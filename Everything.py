import subprocess
from time import sleep
from common_lib import *

#
app_name = 'Everything'


def Everything(app_name, file_name_exe, download_link):
    app_name = 'Everything'
    try:
        # Check app is installed
        result = check_app_existed(app_name)
        if result:
            return True
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
        install_app(install_command,10)
        # Check app install
        for i in range(60):
            result = check_app_existed(app_name)
            if result:
                print('cai dat thanh cong')
                return True
            sleep(5)

    except Exception as e:
        print(f'error install: {e}')
        return False


# if __name__ == '__main__':
#     download_link = 'https://www.voidtools.com/Everything-1.4.1.1026.x64-Setup.exe'
#     Everything(app_name, '', download_link)
    # print(check_app_existed('ALTool'))
    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

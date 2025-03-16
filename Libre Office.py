import subprocess
from time import sleep
from common_lib import *

#
app_name = 'Libre Office'


def Libre_Office(app_name, file_name_exe, download_link):
    app_name = 'Libre Office'
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
        exe_files = [file for file in file_names if
                     file.endswith('.msi') and os.path.isfile(os.path.join(download_directory, file))]
        # Ensure download_directory and file_name_exe are correctly defined earlier in your code
        msi_path = f"{download_directory}\{exe_files[0]}"
        print(msi_path)
        command = [
            "msiexec",
            "/i", msi_path,  # /i for installation
            "/quiet",  # Silent install
            "/norestart"  # Prevent restart after installation
        ]
        # Install app with quoted paths
        install_app(command, 10)
        # Check app install
        for i in range(60):
            result = check_app_existed(app_name)
            if result:
                print('cai dat thanh cong')
                return True
            sleep(10)

    except Exception as e:
        print(f'error install: {e}')
        return False


# if __name__ == '__main__':
#     download_link = 'https://www.libreoffice.org/donate/dl/win-x86_64/25.2.1/ko/LibreOffice_25.2.1_Win_x86-64.msi'
#     Libre_Office(app_name, 'LibreOffice_25.2.1_Win_x86-64.msi', download_link)

    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

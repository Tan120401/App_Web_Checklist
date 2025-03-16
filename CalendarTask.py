from common_lib import *


def CalendarTask(app_name, file_name_exe, download_link):
    app_name = 'CalendarTask'
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
        exe_files = [file for file in file_names if
                     file.endswith('.exe') and os.path.isfile(os.path.join(download_directory, file))]

        # Ensure download_directory and file_name_exe are correctly defined earlier in your code
        installer_command = f'"{download_directory}\{exe_files[0]}" /S'
        # Install app with quoted paths
        install_app(installer_command, 10)
        print('da het thoi gian')
        # Connect app
        # skip
        # Check app install
        for i in range(60):
            result = check_app_existed(app_name)
            if result:
                return True
            sleep(10)

    except Exception as e:
        print(f'error install: {e}')
        return False


# if __name__ == '__main__':
#     download_link = 'https://download.xdiarys.com/windows/xdiarys-setup-v3.exe'
#     Desktop_Calendar(app_name, 'xdiarys-setup-v3.exe', download_link)

    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

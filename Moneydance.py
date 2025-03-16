import subprocess
from time import sleep
from common_lib import *

app_name = 'Moneydance'


def Moneydance(app_name, file_name_exe, download_link):
    app_name = 'Moneydance'
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
        print(install_path)
        # #
        # Install app with quoted paths
        subprocess.Popen(['start', install_path], shell=True)
        sleep(15)
        # click button
        print('qua toi day rooif')
        next_btn_path = os.path.join('res', 'moneydance_nextbutton.png')
        print(next_btn_path)
        for i in range(3):
            try:
                next_position = pyautogui.locateCenterOnScreen(next_btn_path, confidence=0.8)
                if next_position:
                    print(next_position)
                    pyautogui.click(next_position)
                    sleep(2)
            except Exception as e:
                print(e)

        sleep(5)
        finish_btn_path = os.path.join('res', 'moneydance_finish.png')
        try:
            finish_position = pyautogui.locateCenterOnScreen(finish_btn_path, confidence=0.8)
            if finish_position:
                pyautogui.click(finish_position)
                sleep(2)
        except Exception as e:
            print(e)
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

#
# if __name__ == '__main__':
#     download_link = 'https://infinitekind.com/stabledl/current/Moneydance_windows_amd64.exe'
#     Moneydance(app_name, '', download_link)

    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

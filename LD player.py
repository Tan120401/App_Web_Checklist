import subprocess
from time import sleep
from common_lib import *
import platform
#
app_name = 'LDPlayer'

def LD_player(app_name, file_name_exe, download_link):
    app_name = 'LDPlayer'
    try:
        cpu_name = platform.processor()
        print("CPU Name:", cpu_name)
        if 'amr' in cpu_name.lower():
            return True
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
        subprocess.Popen(['start', install_path], shell=True)
        sleep(10)
        # print('toi day khong')
        install_btn_path = os.path.join('res', 'ldplayer_caidatngay.png')
        print(install_btn_path)
        for i in range(10):
            try:
                install_position = pyautogui.locateCenterOnScreen(install_btn_path, confidence=0.8)
                if install_position:
                    print(install_position)
                    pyautogui.click(install_position)
                    sleep(2)
                    break
            except Exception as e:
                print(e)
            sleep(2)
        sleep(5)
        # Check app install
        for i in range(60):
            result = check_app_existed(app_name)
            if result:
                print('cai dat thanh cong')
                sleep(10)
                # Connect to all windows with the given title
                app = Desktop(backend='win32')

                # Get a list of all matching windows
                windows = app.windows()

                # Print the details of each window
                for i, win in enumerate(windows):
                    print(f"Window {i}: {win} - {win.element_info}")
                    if 'Program Compatibility Assistant' in win.window_text():
                        win.close()
                        sleep(2)
                return True
            sleep(5)

    except Exception as e:
        print(f'error install: {e}')
        return False

#
# if __name__ == '__main__':
#     download_link = 'https://res.ldrescdn.com/download/LDPlayer9.exe?n=LDPlayer9_vn_1003_ld.exe'
#     LD_player(app_name, '', download_link)
    # print(check_app_existed('ALTool'))
    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

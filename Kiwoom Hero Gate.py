import subprocess
from time import sleep
from common_lib import *

app_name = 'Kiwoom'


def Kiwoom_Hero_Gate(app_name, file_name_exe, download_link):
    app_name = 'Kiwoom'
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
        sleep(15)
        # print('toi day khong')
        for i in range(15):
            try:
                app = Application(backend='uia').connect(title_re=u'.*Global - InstallShield Wizard')
                setup_window = app.window(title_re=u'.*Global - InstallShield Wizard')
                if setup_window:
                    setup_window.set_focus()
                    sleep(2)
                    break
            except Exception as e:
                print(e)
            sleep(2)
        #     Next
        pyautogui.hotkey('alt', 'n')
        sleep(3)
        #     Next
        pyautogui.hotkey('alt', 'n')
        sleep(3)
        pyautogui.hotkey('alt', 'i')
        # Check app install
        for i in range(60):
            result = check_app_existed(app_name)
            if result:
                print('cai dat thanh cong')
                sleep(10)
                app = Application(backend='uia').connect(title_re=u'.*Global - InstallShield Wizard')
                setup_window = app.window(title_re=u'.*Global - InstallShield Wizard')
                # Connect to all windows with the given title
                setup_window.set_focus()
                sleep(1)
                pyautogui.press('enter')
                return True
            sleep(5)

    except Exception as e:
        print(f'error install: {e}')
        return False


# if __name__ == '__main__':
#     download_link = 'https://download.kiwoom.com/herog_custom/KiwoomGlobalSetup.exe'
#     Kiwoom_Hero_Gate(app_name, '', download_link)
    # print(check_app_existed('ALTool'))
    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

import subprocess
from time import sleep
from common_lib import *

#
app_name = 'Overwolf'


def Overwolf(app_name, file_name_exe, download_link):
    app_name = 'Overwolf'
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
        # Overwolf
        # Installer
        for i in range(15):
            try:
                app = Application(backend='uia').connect(title='Overwolf Installer')
                setup_window = app.window(title='Overwolf Installer')
                # setup_window.print_control_identifiers()
                if setup_window:
                    setup_window.set_focus()
                    # break
                    sleep(2)
                    click_object_by_name('Overwolf Installer',"Next","Button")
                    for i in range(20):
                        accept_text = setup_window.child_window(title="I accept the", control_type='Text')
                        if accept_text.exists():
                            accept_text.click_input()
                            sleep(2)
                            setup_window.child_window(title="Next", control_type='Button').click_input()
                            sleep(3)
                            setup_window.child_window(title="Next", control_type='Button').click_input()
                            for i in range(60):
                                successfully = setup_window.child_window(title='successfully installed', control_type='Text')
                                if successfully.exists():
                                    setup_window.close()
                                    break
                                sleep(5)
                            break
                        sleep(1)
                    break
            except Exception as e:
                print(e)
            sleep(1)
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
#     download_link = 'https://download.overwolf.com/install/Download?utm_source=web_app_store'
#     Overwolf(app_name, '', download_link)

    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

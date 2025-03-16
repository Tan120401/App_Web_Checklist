import subprocess
from time import sleep
from common_lib import *

#
app_name = 'WinZip'


def WinZip(app_name, file_name_exe, download_link):
    app_name = 'WinZip'
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

        # Install app with quoted paths
        subprocess.Popen(f"{install_path}")
        for i in range(15):
            try:
                app = Application(backend='uia').connect(title='Welcome')
                setup_window = app.window(title='Welcome')
                # setup_window.print_control_identifiers()
                if setup_window:
                    setup_window.set_focus()
                    sleep(2)
                    setup_window.child_window(title="Next", control_type="Button").click_input()
                    sleep(1)
                    click_object_by_name('Agreement',"Agree","Button")
                    click_object_by_name('Analytics', "Agree", "Button")
                    sleep(1)
                    for i in range(60):
                        click_object_by_name('Finish', "Finish", "Button")
                        sleep(1)
                    break
            except Exception as e:
                print(e)
            sleep(2)
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
#     download_link = 'https://download.winzip.com/gl/nkln/winzip76-home.exe'
#     Win_zip(app_name, '', download_link)

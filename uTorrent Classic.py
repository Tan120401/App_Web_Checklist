import subprocess
from time import sleep
from common_lib import *

#
app_name = 'Torrent'


def uTorrent_Classic(app_name, file_name_exe, download_link):
    app_name = 'Torrent'

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
        # Chạy lệnh PowerShell mà không cần lấy kết quả
        subprocess.Popen(f"{install_path}")
        sleep(2)
        print('da toi day')
        # print('toi day khong')
        for i in range(15):
            try:
                app = Application(backend='uia').connect(title_re='.*Torrent Classic')
                setup_window = app.window(title_re='.*Torrent Classic')
                # setup_window.print_control_identifiers()
                if setup_window:
                    setup_window.set_focus()
                    # break
                    sleep(2)
                    setup_window.child_window(title="Next", control_type="Button").click_input()
                    sleep(1)
                    for i in range(30):
                        next_btn = setup_window.child_window(title="Next", control_type="Button")
                        if next_btn.exists():
                            next_btn.click_input()
                            sleep(1)
                            setup_window.child_window(title="Agree", control_type="Button").click_input()
                            sleep(1)
                            setup_window.child_window(title="Accept", control_type="Button").click_input()
                            sleep(1)
                            setup_window.child_window(title="Next", control_type="Button").click_input()
                            sleep(1)
                            setup_window.child_window(title="Next", control_type="Button").click_input()
                            break
                        sleep(1)

                    for i in range(60):
                        finish_btn = setup_window.child_window(title="Finish", control_type="Button")
                        if finish_btn.exists():
                            setup_window.child_window(title="Launch the application on exit",
                                                      control_type='CheckBox').click_input()
                            sleep(1)
                            finish_btn.click_input()
                            sleep(2)
                            break
                    break
            except Exception as e:
                print(e)
            sleep(1)
        # Check app install
        for i in range(60):
            result = check_app_existed(app_name)
            if result:
                print('cai dat thanh cong')
                sleep(10)
                return True
            sleep(5)

    except Exception as e:
        print(f'error install: {e}')
        return False
    return True

# if __name__ == '__main__':
#     download_link = 'https://www.utorrent.com/downloads/complete/track/stable/os/win/'
#     uTorrent_Classic(app_name, '', download_link)
    # print(check_app_existed('ALTool'))
    # "C:\Users\ameri\Downloads\Autodesk\DWG TrueView 2025 - English - (EN)\Setup.exe" / silent / install / norestart

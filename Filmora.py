from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app, check_app_installed, \
    check_app_installed_32

def Filmora(app_name, file_name_exe, download_link):
    try:
        # # Check app is installed
        # result = check_program_installed(app_name)
        # if result:
        #     return result
        #
        # # Download and execute install file
        # download_result = download_and_execute(file_name_exe, download_link, 10, 10)
        #
        # # If download and execute fail -> return fail'
        # if not download_result:
        #     return download_result

        #Connect app
        target_window = connect_app('Wondershare Filmora')
        print(target_window.print_control_identifiers())
        # Check app install
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Filmora('Filmora', 'filmora_setup_full6119.exe', 'https://download.wondershare.kr/filmora_full6119.exe')
print(result)
'https://support.image-line.com/redirect/flstudio_win_installer?_gl=1*g4ilmg*_gcl_au*NTcxNjY4OTM3LjE3NDA5OTQ1NTg.'
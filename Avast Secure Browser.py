from time import sleep

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows, click_object_by_index, click_object, click_without_id, close_app

def Avast_Secure_Browser(app_name, file_name_exe, download_link):
    try:
        # # Check app is installed
        # result = check_program_installed(app_name)
        # if result:
        #     return result
        #
        # # Download and execute install file
        # download_result = download_and_execute(file_name_exe, download_link, 5, 10)
        #
        # # If download and execute fail -> return fail
        # if not download_result:
        #     return download_result

        #Connect app
        target_window = connect_app('Avast Secure Browser')
        print(target_window.print_control_identifiers())

        # Check app install
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Avast_Secure_Browser('Avast Secure Browser', 'avast_secure_browser_setup.exe', 'https://www.softonic.kr/download-launch?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb3dubG9hZFR5cGUiOiJleHRlcm5hbERvd25sb2FkIiwiZG93bmxvYWRVcmwiOiJodHRwczovL2Nkbi1kb3dubG9hZC5hdmFzdGJyb3dzZXIuY29tL3NvZnRvbmljL2F2YXN0X3NlY3VyZV9icm93c2VyX3NldHVwLmV4ZSIsImFwcElkIjoiYTlhMjJlMzgtYTRkNC0xMWU2LTg5NGMtMDAxNjNlZDgzM2U3IiwicGxhdGZvcm1JZCI6IndpbmRvd3MiLCJpYXQiOjE3NDA5NzI0OTcsImV4cCI6MTc0MDk3NjA5N30.dTKBLZf0jWOD2mnKKuEqTHqA1EoEVMre2qPRZgDmHxY')
print(result)
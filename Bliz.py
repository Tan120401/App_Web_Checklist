

from common_lib import download_by_link, run_file_exe, check_program_installed, download_and_execute, connect_app, \
    print_all_windows


def Bliz(app_name, file_name_exe, download_link):
    try:
        #Check app is installed
        result = check_program_installed(app_name)
        if result:
            return result

        #Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 20, 10)

        #If download and excute fail -> return fail
        if not download_result:
            return download_result

        #Wait for installation
        sleep(20)

        #Check app is installed
        return True
    except Exception as e:
        print(f'error install: {e}')
        return False
result = Bliz('Blitz', 'Blitz-2.1.267.exe', 'https://blitz.gg/download/win')
print(result)
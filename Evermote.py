import os

from time import sleep

from common_lib import download_by_link, run_file_exe, download_and_execute, check_program_installed


def Evermote(app_name, file_name_exe, download_link):
    try:
        result = download_and_execute(app_name, file_name_exe, download_link, 12, 5)
        if result:
            return result
        # wait for install done
        sleep(90)
        result = check_program_installed(app_name)
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
Evermote('Evermote', 'Evernote-latest.exe', 'https://win.desktop.evernote.com/builds/Evernote-latest.exe')
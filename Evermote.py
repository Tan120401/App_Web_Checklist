import os

from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'Evernote-latest.exe')

if not os.path.isfile(file_path):
    download_by_link('https://win.desktop.evernote.com/builds/Evernote-latest.exe')
    sleep(90)

run_file_exe(file_path)
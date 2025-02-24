import os

from time import sleep

from common_lib import download_by_link, run_file_exe

()

# Đường dẫn đến tệp thực thi
file_path = os.path.join(download_directory, 'DropboxInstaller.exe')

if not os.path.isfile(file_path):
    download_by_link('https://dl-web.dropbox.com/installer?arch=x86_64&authenticode_sign=True&build_no=218.4.4348&juno=True&juno_use_program_files=True&omaha=True&omaha_use_program_files=True&plat=win&tag=eyJUQUdTIjoiZUp5clZpcE9MUzdPek0tTHoweFJzbEl3TlRFeE1qSXl0ekN4TkRNM05UQTB0REEwTVRJek1EUTFNalcyTkRRMU1ESTBOTFUwTnFvRkFKc1VEWFV-QE1FVEEifQ&tag_token=AgSUCkxdvsAaMv3mTcZhPII-gCEHcXYf7IqCPIGb8yzwdA')
    sleep(10)

run_file_exe(file_path)
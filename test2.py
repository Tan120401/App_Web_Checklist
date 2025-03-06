import subprocess

from common_lib import base_install_by_microsoft_store, connect_app, check_app_existed
#
result = base_install_by_microsoft_store('BreeZip: RAR & ZIP Extractor')
print(result)

# result = base_install_by_microsoft_store('Mail')
# print(result)

# target_window = connect_app('Microsoft Store')
# print(target_window.print_control_identifiers())
#
# print(check_app_existed('Citrix Workspace'))

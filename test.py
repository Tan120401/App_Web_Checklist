from pywinauto import Desktop
from pywinauto.findwindows import find_windows

from common_lib import check_program_installed, print_all_windows, run_file_exe

# result = check_program_installed('알송')
# print(result)

# def IPinsideLWS():
#     try:
#         result = check_program_installed('IPinside LWS Agent')
#         if result:
#             return result
#         # Đường dẫn đến tệp thực thi
#         file_path = os.path.join(download_directory, 'APS_Engine.exe')
#
#         if not os.path.isfile(file_path):
#             download_by_link('https://mybank.ibk.co.kr/IBK/uib/sw/yettiesoft/APS/APS_Engine.exe')
#             sleep(10)
#
#         # Hàm kiểm tra xem nếu đã tồn tại file cài đặt thì run nó
#         run_file_exe(file_path)
#         sleep(2)
#         # Kết nối tới màn hình cài đặt app
#         # target_window = connect_app('APS Engine')
#         #
#         # #Click next
#         # click_object(target_window, '´ÙÀ½ >', '1', 'Button')
#         #
#         # # Kiem tra xem da cai dat thanh cong hay chua
#         # result = check_program_installed('APS Engine')
#         # return result
#     except Exception as e:
#         print(f'error install: {e}')
#         return False

print_all_windows()


# from pywinauto import Application, Desktop
#
# # Kết nối với cửa sổ 'Battle.net Setup'
# app = Application(backend="uia").connect(title="Battle.net Setup")
# dlg = app.window(title="Battle.net Setup")
# print(dlg.print_control_identifiers())

# Tìm và click vào nút 'Continue'
# continue_button = dlg.child_window(title="Continue", control_type="Button")
#
# # Kiểm tra nếu nút 'Continue' tồn tại và click vào nó
# if continue_button.exists():
#     continue_button.click()
#     print("Đã click vào nút 'Continue'")
# else:
#     print("Không tìm thấy nút 'Continue'")


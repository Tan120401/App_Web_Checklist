from pywinauto import Desktop


from common_lib import check_program_installed, print_all_windows

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
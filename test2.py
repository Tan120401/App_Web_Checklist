import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from common_lib import get_download_folder
#
#
# # Định nghĩa hàm để lấy tên tệp vừa tải về
# class DownloadHandler(FileSystemEventHandler):
#     def __init__(self):
#         self.latest_file = None
#
#     def on_created(self, event):
#         if not event.is_directory:
#             self.latest_file = event.src_path
#
# def download_by_link(link):
#     # Tạo tùy chọn cho Chrome
#     download_folder = get_download_folder()
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     # Cấu hình bỏ qua xác nhận người dùng, tự động down load về folder down load
#     prefs = {"download.default_directory": download_folder,
#              "download.prompt_for_download": False,  # Chrome sẽ không hiện cửa sổ xác nhận trước khi tải xuống tệp.
#              "profile.default_content_setting_values.automatic_downloads": 1,
#              # cho phép tải xuống tự động mà không bị chặn.
#              "safebrowsing.enabled": True}  # kích hoạt tính năng Bảo mật An toàn (Safe Browsing) của Chrome
#     chrome_options.add_experimental_option("prefs", prefs)
#
#     # Khởi tạo trình điều khiển cho Chrome
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#
#     # Thiết lập theo dõi thư mục tải về
#     event_handler = DownloadHandler()
#     observer = Observer()
#
#     observer.schedule(event_handler, path=download_folder, recursive=False)
#     observer.start()
#
#     # Mở một trang web và tải xuống tệp
#     driver.get(link)
#     time.sleep(10)  # Đợi để đảm bảo tệp đã tải về xong, thời gian này có thể điều chỉnh tùy theo kích thước tệp
#
#     # Dừng theo dõi thư mục
#     observer.stop()
#     observer.join()
#
#     # Lấy tên tệp vừa tải về
#     latest_file = event_handler.latest_file
#     return latest_file
#
# # Ví dụ sử dụng
# link = "https://www.blizzard.com/download/confirmation?product=bnetdesk"
# downloaded_file = download_by_link(link)
# print(f"Tệp vừa tải về: {downloaded_file}")
import os



download_folder = get_download_folder()  # Thư mục tải về của bạn
latest_file = get_latest_file(download_folder)
print(latest_file)

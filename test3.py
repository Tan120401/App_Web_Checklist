import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def download_by_link(link, timeout=3600):
    # Xác định thư mục Downloads
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    # Tạo tùy chọn cho Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')

    # Cấu hình bỏ qua xác nhận người dùng, tự động tải xuống về thư mục Downloads
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "profile.default_content_setting_values.automatic_downloads": 1,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Khởi tạo trình điều khiển cho Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Lấy danh sách các tệp trong thư mục Downloads trước khi tải xuống
    files_before = set(os.listdir(download_dir))

    # Mở liên kết để bắt đầu tải xuống
    driver.get(link)

    # Đợi cho đến khi có tệp mới trong thư mục Downloads
    start_time = time.time()
    downloaded_file = None
    downloading_extensions = [".crdownload", ".tmp", ".partial"]

    while time.time() - start_time < timeout:
        # Kiểm tra các tệp hiện tại
        files_now = set(os.listdir(download_dir))
        new_files = files_now - files_before

        # Kiểm tra xem có tệp đang tải không
        downloading_files = [f for f in new_files if any(f.endswith(ext) for ext in downloading_extensions)]

        # Kiểm tra xem có tệp đã tải xuống hoàn tất không
        completed_files = [f for f in new_files if not any(f.endswith(ext) for ext in downloading_extensions)]

        if downloading_files:
            print(f"Đang tải xuống: {downloading_files}")

        if completed_files:
            downloaded_file = completed_files[0] if completed_files else None
            if downloaded_file:
                print(f"Tải xuống hoàn tất: {downloaded_file}")
                break

        # Tạm dừng một chút trước khi kiểm tra lại
        time.sleep(10)

    if downloaded_file:
        print(f"Tải xuống thành công: {os.path.join(download_dir, downloaded_file)}")
    else:
        print("Hết thời gian chờ hoặc không phát hiện tệp tải xuống")

    return driver

download_by_link('https://www.clipstudio.net/en/purchase/complete_win/')
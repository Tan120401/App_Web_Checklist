import codecs
import os
import platform
import time
from datetime import datetime
from time import sleep
import subprocess

import pandas as pd
import pyautogui
from AppOpener import open
from pywinauto import Application, Desktop

import random

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Function to write logs
def write_log(testcase_name,pass_list, fail_list, log_file_name):
    # Open log file and write
    try:
        log_folder = 'Log_folder_Sound_Config'
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # Full path for the log file
        log_file_path = os.path.join(log_folder, log_file_name)
        with codecs.open(f"{log_file_path}", "a", "utf-8") as file:
            file.write(f"*{testcase_name.upper()}\n")
            file.write("-List of pass: \n")
            file.write("\n".join(pass_list))
            file.write("\n")
            if len(fail_list) > 0:
                file.write("-List of fail: \n")
                file.write("\n".join(fail_list))
                file.write("\n")
            file.write("-------------------------------------------------------------------------\n")
    except Exception as e:
        print(f'Write log error: {e}')

# Function init log file
def init_log_file():
    # change_global_log_file()
    now = datetime.now()
    current_time = now.strftime('%m%d%Y_%H%M%S')
    print(current_time)
    global log_file_name
    log_file_name = f"{current_time}_SOUND_CONFIG.txt"

    # check setting log exists
    if os.path.exists(log_file_name):
        try:
            # delete file
            os.remove(log_file_name)
            print(f"Deleted existing log file: {log_file_name}")
            return log_file_name
        except Exception as e:
            print(f"Error deleting log file: {e}")
    try:
        # Khởi tạo lại file log
        with codecs.open(log_file_name, "w", "utf-8") as file:
            file.write("")  # Tạo file rỗng
        print(f"Initialized new log file: {log_file_name}")
        return log_file_name
    except Exception as e:
        print(f"Error initializing log file: {e}")

# Function init report file name
def init_file_name():
    now = datetime.now()
    current_time = now.strftime('%m%d%Y_%H%M%S')
    report_file_name = f"{current_time}_SOUND_CONFIG_REPORT.xlsx"
    log_file_name = f"{current_time}_SOUND_CONFIG_REPORT.txt"
    return [log_file_name, report_file_name]

#Function write result to excel file
def write_result_report(testcase_name, result, report_file_name):
    log_folder = 'Log_folder_Sound_Config'
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # Full path for the log file
    log_file_path = os.path.join(log_folder, report_file_name)
    data_report = {
        'Test Case': testcase_name,
        'Result': result
    }
    df = pd.DataFrame(data_report)

    df.to_excel(log_file_path, sheet_name='Sound Config', index=False, engine='openpyxl')

    # Read back the file to verify
    dfread = pd.read_excel(log_file_path, sheet_name='Sound Config')
    print(dfread)

#Function click by id
def click_by_id(driver, id):
    element = driver.find_element(By.ID, id)
    print('display', element.is_displayed())
    element.click()

#Function connect chrome
def link_search(link):
    # Đường dẫn tới Chrome WebDriver đã tải về
    chrome_driver_path = "chromedriver.exe"
    # Khởi tạo dịch vụ Chrome WebDriver
    service = Service(executable_path=chrome_driver_path)

    # Cấu hình các tùy chọn cho Chrome

    # Danh sách User-Agent
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
        # Thêm nhiều User-Agent khác nếu cần
    ]

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\NST\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    options.add_argument("--start-maximized")
    options.add_argument("--enable-features=EnhancedProtection")
    options.add_argument(f"user-agent={random.choice(user_agents)}")

    # Khởi tạo trình điều khiển (driver) cho Chrome
    driver = webdriver.Chrome(service=service, options=options)

    # Mở trang web Google
    driver.get(f"{link}")

    return driver

#Function click by Xpath
def click_by_xpath(driver, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        if element:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print('display', element.is_displayed())
            element.click()
            return True
        return False
    except Exception as e:
        # print(f'Click by xpath error: {e}')
        return False


# Function get folder
def get_download_folder():
    if platform.system() == "Windows":
        download_folder = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
    elif platform.system() == "Darwin":  # macOS
        download_folder = os.path.join(os.getenv('HOME'), 'Downloads')
    else:  # Linux and other Unix-like systems
        download_folder = os.path.join(os.getenv('HOME'), 'Downloads')
    return download_folder
download_directory = get_download_folder()

#Get latest file download
def get_latest_file():
    while True:
        files = os.listdir(download_directory)
        if files:
            files = [os.path.join(download_directory, f) for f in files if not f.endswith('.tmp')]
            files.sort(key=os.path.getctime, reverse=True)
            if files:
                return files[0]
        time.sleep(1)

# Function download app by link
def download_by_link(link):
    # Tạo tùy chọn cho Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Cấu hình bỏ qua xác nhận người dùng, tự động down load về folder down load
    prefs = {"download.default_directory": "Downloads",
             "download.prompt_for_download": False,  # Chrome sẽ không hiện cửa sổ xác nhận trước khi tải xuống tệp.
             "profile.default_content_setting_values.automatic_downloads": 1,
             # cho phép tải xuống tự động mà không bị chặn.
             "safebrowsing.enabled": True}  # kích hoạt tính năng Bảo mật An toàn (Safe Browsing) của Chrome
    chrome_options.add_experimental_option("prefs", prefs)

    # Khởi tạo trình điều khiển cho Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Mở một trang web
    driver.get(f'{link}')
    return driver

# Run file exe
# Kiểm tra lại xem tệp đã tồn tại chưa
def run_file_exe(file_path):
    try:
        # subprocess.run sẽ chờ cho tiến trình con chạy xong
        # subprocess.Popen chỉ chạy file exe mà không chờ các tiến trình con chạy xong
        if os.path.isfile(file_path):
            print('Tệp đã được tải xuống. Đang chạy tệp...')
            if platform.system() == "Windows":
                process =  subprocess.Popen([file_path], shell=True)
            elif platform.system() == "Darwin":
                process =  subprocess.Popen(["open", file_path])
            else:
                process =  subprocess.Popen(["xdg-open", file_path])
        else:
            print('Tệp chưa được tải xuống thành công.')
    except Exception as e:
        print(f'error run file install: {e}')

# Function close app
def close_app(app_name):
    try:
        app = Application(backend='uia').connect(title_re=app_name)
        target_window = app.window(title_re=app_name)
        target_window.close()
    except Exception as e:
        print(f'close app error: {e}')

# Function open app return target windows
def connect_app(app_name):
    try:
        app = Application(backend='uia').connect(title_re=f'.*{app_name}.*')
        target_window = app.window(title_re=f'.*{app_name}.*')
        return target_window
    except Exception as e:
        print(f'connect app error: {e}')

def wait_until(timeout, interval, condition):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if condition():
            return True
        time.sleep(interval)
    raise TimeoutError("Time out error")

# Function click object exist
def click_object(window, title, auto_id, control_type):
    object_select = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    try:
        wait_until(5, 1, lambda: object_select.exists())
        object_select.click_input()
        result = [True, title, object_select]
    except TimeoutError as e:
        print(f'Click error: {e}')
        result = [False, title, None]
    sleep(1)
    return result

# Function click object by index
def click_object_by_index(window, title, control_type, index):
    try:
        object_selects = window.descendants(title=title, control_type=control_type)
        object_select = object_selects[index]
        wait_until(5, 1, lambda: object_select.is_visible())
        object_select.click_input()
        result = [True, title, object_select]
    except Exception as e:
        print(f"Error clicking object: {e}")
        return (False, title, None)
    sleep(1)
    return result

# Function click object exist
def click_without_id(window, title, control_type):
    object_select = window.child_window(title=title, control_type=control_type)
    try:
        wait_until(5, 1, lambda: object_select.exists())
        object_select.click_input()
        result = [True, title, object_select]
    except TimeoutError as e:
        print(f'Click error: {e}')
        result = [False, title, None]
    sleep(1)
    return result

# Function click without title
def click_without_title(window, auto_id, control_type):
    object_select = window.child_window(auto_id=auto_id, control_type=control_type)
    try:
        wait_until(5, 1, lambda: object_select.exists())
        object_select.click_input()
        result = [True, object_select]
    except TimeoutError as e:
        print(f'Click error: {e}')
        result = [False, None]
    sleep(1)
    return result

# Function find object
def find_object(window, title, auto_id, control_type):
    object_find = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    try:
        wait_until(5, 0.5, lambda: object_find.exists())
        result = [True, title, object_find]
    except Exception as e:
        print(f'Find Object error: {title, e}')
        result = [False, title, None]
    return result

import winreg

def check_program_installed(program_name):
    # Mở khóa registry chính của các chương trình cài đặt trên hệ thống 64-bit
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)

    # Kiểm tra các chương trình cài đặt
    for i in range(winreg.QueryInfoKey(key)[0]):
        sub_key_name = winreg.EnumKey(key, i)
        sub_key = winreg.OpenKey(key, sub_key_name)
        try:
            display_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
            if program_name.lower() in display_name.lower():
                return True
        except FileNotFoundError:
            pass
        finally:
            sub_key.Close()

    # Kiểm tra các chương trình 32-bit trên hệ thống 64-bit
    key_path_32bit = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    key_32bit = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path_32bit)

    # Kiểm tra các chương trình cài đặt
    for i in range(winreg.QueryInfoKey(key_32bit)[0]):
        sub_key_name = winreg.EnumKey(key_32bit, i)
        sub_key = winreg.OpenKey(key_32bit, sub_key_name)
        try:
            display_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
            if program_name.lower() in display_name.lower():
                return True
        except FileNotFoundError:
            pass
        finally:
            sub_key.Close()

    return False

# Print all windows
def print_all_windows():
    desktop = Desktop(backend='uia')
    all_windows = desktop.windows()
    for win in all_windows:
        print(win.window_text())

# Download and run file install
def download_and_execute(file_name_exe, download_link, time_wait_download, time_wait_execute):
    try:

        # Đường dẫn đến tệp thực thi
        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            #Down load thông qua link
            download_by_link(download_link)
            sleep(time_wait_download)
        file_path = get_latest_file()
        # Hàm kiểm tra xem nếu đã tồn tại file cài đặt thì run nó
        run_file_exe(file_path)
        sleep(time_wait_execute)
        return True
    except Exception as e:
        print(f'Download and run error: {e}')
        return False

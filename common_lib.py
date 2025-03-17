import os
import platform
import time
from time import sleep
import subprocess
import winreg

import pyautogui
from AppOpener import open
from pywinauto import Application, Desktop, findwindows

import random

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
def download_by_link(link, timeout = 3600):
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

    try:
        # Lấy danh sách các tệp trong thư mục Downloads trước khi tải xuống
        files_before = set(os.listdir(download_dir))

        # Mở liên kết để bắt đầu tải xuống
        driver.get(link)
        print(f"Đã bắt đầu tải xuống từ: {link}")

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
            return True
        else:
            print("Hết thời gian chờ hoặc không phát hiện tệp tải xuống")
            return False

    finally:
        # Đảm bảo driver luôn được đóng dù có lỗi hay không
        print("Đóng trình duyệt Chrome...")
        driver.quit()

# Function get link
def get_link(link):
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

    driver.get(link)
    return driver

# Run file exe
def run_file_exe(file_path):
    try:
        # subprocess.run sẽ chờ cho tiến trình con chạy xong
        # subprocess.Popen chỉ chạy file exe mà không chờ các tiến trình con chạy xong
        if os.path.isfile(file_path):
            print(f'Tệp đã được tải xuống. {file_path} Đang chạy tệp...')
            if platform.system() == "Windows":
                process =  subprocess.Popen(f'"{file_path}"', shell=True)
            elif platform.system() == "Darwin":
                process =  subprocess.Popen(["open", file_path])
            else:
                process =  subprocess.Popen(["xdg-open", file_path])
        else:
            print('Tệp chưa được tải xuống thành công.')
    except Exception as e:
        print(f'error run file install: {e}')

def run_file_exe_by_run(file_path):
    try:
        # subprocess.run sẽ chờ cho tiến trình con chạy xong
        # subprocess.Popen chỉ chạy file exe mà không chờ các tiến trình con chạy xong
        if os.path.isfile(file_path):
            print(f'Tệp đã được tải xuống. {file_path} Đang chạy tệp...')
            if platform.system() == "Windows":
                process =  subprocess.run(f'"{file_path}"', shell=True)
            elif platform.system() == "Darwin":
                process =  subprocess.run(["open", file_path])
            else:
                process =  subprocess.run(["xdg-open", file_path])
        else:
            print('Tệp chưa được tải xuống thành công.')
    except Exception as e:
        print(f'error run file install: {e}')

# Function open app return target windows
def open_app(app_name):
    try:
        all_window_active = Desktop(backend='uia').windows()
        for win in all_window_active:
            if win.window_text() == app_name:
                close_app(app_name)

        open(app_name, match_closest=False)
        sleep(3)
        app = Application(backend='uia').connect(title_re=app_name)
        target_window = app.window(title_re=app_name)
        return target_window
    except Exception as e:
        print(f'open app error: {e}')

# Function close app
def close_app(app_name):
    try:
        app = Application(backend='uia').connect(title_re=f".*{app_name}.*")
        target_window = app.window(title_re=f".*{app_name}.*")
        target_window.close()
    except Exception as e:
        print(f'close app error: {e}')

# Function open app return target windows
def connect_app(app_name):
    try:
        app = Application(backend='uia').connect(title_re=f'.*{app_name}.*')
        target_window = app.window(title_re=f'.*{app_name}.*')
        target_window.set_focus()
        return target_window
    except Exception as e:
        print(f'connect app error: {e}')
        return False

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
        object_select.invoke()
        result = [True, title, object_select]
    except TimeoutError as e:
        print(f'Click error: {e}')
        result = [False, title, None]
    sleep(1)
    return result

# Function click object by image
def click_object_by_image(file_path, confidence_value  = 0.9):
    print('da vao day')
    object_select = pyautogui.locateCenterOnScreen(file_path, confidence=confidence_value)

    print(object_select)
    try:
        wait_until(5, 1, lambda: object_select)
        pyautogui.click(object_select)
        result = True
    except TimeoutError as e:
        print(f'Click error: {e}')
        result = False
    sleep(1)
    return result

# Function click object exist
def click_object_click_input(window, title, auto_id, control_type):
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

# Function click object exist
def click_app(window, title, control_type):
    object_select = window.child_window(title_re=f'{title}. .*', control_type=control_type)
    try:
        wait_until(5, 1, lambda: object_select.exists())
        object_select.click_input()
        result = [True, title, object_select]
    except TimeoutError as e:
        print(f'Click error: {e}')
        result = [False, title, None]
    sleep(1)
    return result


def click_app_by_index(window, title, control_type, index=0):
    import re

    # Lấy tất cả các phần tử có control_type đã chỉ định
    all_elements = window.descendants(control_type=control_type)

    # Tạo mẫu regex
    pattern = re.compile(f'{re.escape(title)}.*')

    # Lọc các phần tử có tiêu đề khớp với mẫu
    matching_elements = []
    for elem in all_elements:
        try:
            text = elem.window_text()
            if pattern.match(text):
                matching_elements.append(elem)
        except:
            continue

    # Kiểm tra nếu có phần tử phù hợp
    if not matching_elements or index >= len(matching_elements):
        print(f"Không tìm thấy phần tử với title '{title}' và control_type '{control_type}'")
        return [False, title, None]

    # Chọn phần tử ở vị trí index
    object_select = matching_elements[index]

    try:
        wait_until(5, 1, lambda: object_select)
        object_select.click_input()
        result = [True, title, object_select]
    except TimeoutError as e:
        print(f'Click error: {e}')
        result = [False, title, None]
    sleep(1)
    return result
# Function click object exist
def click_input_without_id(window, title, control_type):
    object_select = window.child_window(title=title, control_type=control_type)
    try:
        wait_until(3, 1, lambda: object_select.exists())
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
        object_select.invoke()
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

# Function find object
def find_object_without_id(window, title, control_type):
    object_find = window.child_window(title=title, control_type=control_type)
    try:
        wait_until(5, 0.5, lambda: object_find.exists())
        result = True
    except Exception as e:
        print(f'Find Object error: {title, e}')
        result = False
    return result

# Check App and program installed
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

#Check app installed by microsoft
def is_app_installed(app_name):
    try:
        # Chạy PowerShell để lấy danh sách các ứng dụng đã cài đặt
        command = "powershell Get-StartApps"
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        # Xử lý kết quả để kiểm tra tên hiển thị
        appname = app_name.replace(' ', '')
        installed_apps = result.stdout.lower()  # Đưa toàn bộ kết quả về chữ thường
        if appname.lower() in installed_apps:  # Kiểm tra nếu tên ứng dụng tồn tại
            return True
        return False
    except Exception as e:
        print("Error:", e)
        return False

#Check exist app
def check_app_existed(app_name):
    import subprocess

    # PowerShell command to get the list of installed apps
    command_get_app_list = ["powershell", "-Command", "Get-StartApps"]

    # Run the command with text mode, UTF-8 encoding, and error handling
    result = subprocess.run(command_get_app_list, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if result.stderr:
        print("Errors:", result.stderr)

    # Split the output into a list of app names
    app_list = result.stdout.strip().split('\n')

    # Normalize app_name by removing spaces
    app_name_temp = app_name.replace(' ', '')

    # Iterate through the app list to find a match
    for each_app in app_list:
        if app_name_temp in each_app or app_name in each_app:
            # If a match is found, extract the app ID (text after the last space)
            app_id = each_app.strip().split()[-1]
            # print(f"App existed. Found app ID: {app_id}")
            return True

    # Return None if no match is found
    return None

#Check app install 64 bit
def check_app_installed(app_name):
    file_path = r"C:\Program Files (x86)"
    for root, dirs, files in os.walk(file_path):
        for dir_name in dirs:
            if app_name.lower() in dir_name.lower():
                return True
    return False

#Check app install 32 bit
def check_app_installed_32(app_name):
    file_path = r"C:\Program Files"
    for root, dirs, files in os.walk(file_path):
        for dir_name in dirs:
            if app_name.lower() in dir_name.lower():
                return True
    return False

# Print all windows
def print_all_windows():
    desktop = Desktop(backend='uia')
    all_windows = desktop.windows()
    for win in all_windows:
        print(win.window_text())

# Download and run file install
def download_and_execute(file_name_exe, download_link, time_wait_execute):
    try:

        # Đường dẫn đến tệp thực thi
        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            #Down load thông qua link
            download_by_link(download_link)
            file_path = get_latest_file()

        # Hàm kiểm tra xem nếu đã tồn tại file cài đặt thì run nó
        run_file_exe(file_path)
        sleep(time_wait_execute)
        return True
    except Exception as e:
        print(f'Download and run error: {e}')
        return False

# Download and run file install
def install_app_by_cmd(file_path, handle):
    try:
        # Đường dẫn đến tệp thực thi
        if os.path.isfile(file_path):
            install_silent = [file_path, handle]
            subprocess.run(install_silent, shell=True)
    except Exception as e:
        print(f'Download and run error: {e}')

# Download and run file install
def download_exe_file(file_name_exe, download_link):
    try:

        # Đường dẫn đến tệp thực thi
        file_path = os.path.join(download_directory, file_name_exe)
        if not os.path.isfile(file_path):
            #Down load thông qua link
            download_by_link(download_link)
            file_path = get_latest_file()
        # Hàm kiểm tra xem nếu đã tồn tại file cài đặt thì run nó
        return file_path
    except Exception as e:
        print(f'Download and run error: {e}')
        return False

# Function click element in group
def click_object_within_group(group, name, auto_id, control_type):
    # get all element
    child_elements = group.descendants(control_type=control_type)
    # find elements
    for element in child_elements:
        if element.window_text() == name and element.automation_id() == auto_id:
            return element.click_input()
    return False

#Download app by microsoft store
def base_install_by_microsoft_store(app_name):
    #Check app installed
    if check_app_existed(app_name):
        return True

    #Open Microsoft Store
    target_window = open_app('Microsoft Store')
    click_input_without_id(target_window, 'Search', 'Group')

    #Input app name and search
    key_search = app_name.lower()
    pyautogui.write(key_search, interval=0.01)
    pyautogui.press('enter')
    sleep(3)

    #Select the searched app
    if app_name == 'TikTok' or app_name == 'Discord' or app_name == 'Sway':
        click_app_by_index(target_window, app_name, 'Button')
    elif app_name == 'Pinterest':
        click_app(target_window, 'Microsoft Store Awards 2024. Pinterest', 'Button')
    else:
        click_app(target_window, app_name, 'Button')
    sleep(2)

    #Click install or get
    click_install = click_input_without_id(target_window, 'Install ' , 'Button')
    if not click_install[0]:
        click_get = click_input_without_id(target_window, 'Get ', 'Button')

    #Check installation success by button change to open
    for i in range(100):
        target_window = connect_app('Microsoft Store')
        sleep(5)
        open_button = target_window.child_window(auto_id = 'OpenInstalledProduct', control_type = 'Button')
        disable_install = target_window.child_window(auto_id="InstalledActionDisabled", control_type="Button")
        if open_button.exists() or disable_install.exists():
            return True

#ba.dao

def make_folder_log(folder_path):
    # Kiểm tra và tạo thư mục nếu chưa tồn tại
    os.makedirs(folder_path, exist_ok=True)
    print(f"Thư mục đã được tạo tại: {folder_path}")

def download_app(download_folder, download_link):
    try:
        if any((f.lower().endswith('.exe') or f.lower().endswith('.msi') or f.lower().endswith('.zip'))  and os.path.isfile(
                os.path.join(download_folder, f)) for f in os.listdir(download_folder)):
            print("Thư mục chứa file.")

            return True
        download_to_folder(download_link,download_folder,360)

        # Kiểm tra xem thư mục có chứa file không
        if any((f.lower().endswith('.exe') or f.lower().endswith('.msi') or f.lower().endswith('.zip')) and os.path.isfile(os.path.join(download_folder, f)) for f in os.listdir(download_folder)):
            print("Thư mục chứa file.")
            return True
        else:
            print("Thư mục không chứa file.")
            return False

    except Exception as e:
        print(f'Download and run error: {e}')
        return False

# Function download app by link
def download_to_folder(link,download_folder,wait_time):
    # Tạo tùy chọn cho Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    # Cấu hình bỏ qua xác nhận người dùng, tự động down load về folder down load
    prefs = {"download.default_directory": download_folder,
             "download.prompt_for_download": False,  # Chrome sẽ không hiện cửa sổ xác nhận trước khi tải xuống tệp.
             "profile.default_content_setting_values.automatic_downloads": 1,
             # cho phép tải xuống tự động mà không bị chặn.
             "safebrowsing.enabled": True}  # kích hoạt tính năng Bảo mật An toàn (Safe Browsing) của Chrome
    chrome_options.add_experimental_option("prefs", prefs)

    # Khởi tạo trình điều khiển cho Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Mở một trang web
    driver.get(link)
    for i in range(wait_time):
        # Kiểm tra xem thư mục có chứa file không
        # if any(f.lower().endswith('.exe') and os.path.isfile(os.path.join(download_folder, f)) for f in
        #        os.listdir(download_folder)):
        if any((f.endswith('.exe') or f.endswith('.msi')) and os.path.isfile(
                             os.path.join(download_folder, f)) for f in os.listdir(download_folder)):
            print("File download successfully")
            driver.quit()
            sleep(1)
            return True
        sleep(10)
    else:
        print("File download not successfully")
        driver.quit()
        return False

def find_installed_program(program_name_to_find):
    # Define the registry keys for 64-bit and 32-bit programs
    reg_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",  # For 64-bit
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"  # For 32-bit on 64-bit systems
    ]

    for reg_path in reg_paths:
        try:
            # Open the registry key
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)

            # Iterate through the keys
            for i in range(0, winreg.QueryInfoKey(reg_key)[0]):
                subkey_name = winreg.EnumKey(reg_key, i)
                subkey = winreg.OpenKey(reg_key, subkey_name)

                try:
                    # Try to fetch the DisplayName value (program name)
                    program_name, _ = winreg.QueryValueEx(subkey, "DisplayName")

                    # Check if the program name matches the one we're searching for
                    if program_name_to_find.lower() in program_name.lower():
                        return True,program_name
                except FileNotFoundError:
                    pass
                finally:
                    winreg.CloseKey(subkey)
            winreg.CloseKey(reg_key)
        except FileNotFoundError:
            pass

    # If we finish the loop without finding the program, return False
    return False,program_name_to_find

def install_app(command, sleep_time):
    # Run the command in normal mode
    subprocess.Popen(command, shell=True)
    sleep(sleep_time)  # Adding sleep if needed for timing

def install_msi(msi_path,command):
    try:
        # Define the msiexec command with arguments
        # command = [
        #     "msiexec",
        #     "/i", msi_path,  # /i for installation
        #     "/quiet",  # Silent install
        #     "/norestart"  # Prevent restart after installation
        # ]

        # Run the command using subprocess
        subprocess.run(command, check=True)
        print("Installation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")
    except FileNotFoundError:
        print("msiexec is not found. Make sure you're running on a Windows system.")

def click_object_2(window, title=None, auto_id=None, control_type=None,found_index=0):
    """
    Click vào nút (button) trong cửa sổ ứng dụng.

    :param window: Đối tượng cửa sổ ứng dụng.
    :param title: Tiêu đề của nút (button).
    :param auto_id: ID tự động của phần tử.
    :param control_type: Loại điều khiển (ví dụ: 'Button').
    """

    # Tạo từ điển các tham số để tìm kiếm
    search_params = {}
    if title is not None:
        search_params['title'] = title
    if auto_id is not None:
        search_params['auto_id'] = auto_id
    if control_type is not None:
        search_params['control_type'] = control_type
    search_params['found_index'] = found_index

    # Tìm button với các tham số tìm kiếm
    button = window.child_window(**search_params)

    # Nếu tìm thấy button, click vào nó
    if button.exists(timeout=5):
        button.click_input()
        sleep(1)
    else:
        print(f"Không tìm thấy button với các tham số đã cho.{title}{auto_id}{control_type}")

def get_all_child(window,class_name=None,auto_id=None):
    child_list =[]
    def list_all_children(window):
        children = window.children()  # Get all child controls
        for child in children:
            print(child.class_name())
            if (class_name and child.class_name() == class_name) or (auto_id and child.automation_id() == auto_id) or (not class_name and not auto_id):
                child_list.append(child)  # Add child to the list
            # Recursively list child windows of the current child (if any)
            list_all_children(child)

    list_all_children(window)
    return child_list
def get_all_child_obj(window,class_name=None,auto_id=None):
    child_list =[]
    def list_all_children(window):
        children = window.children()  # Get all child controls
        for child in children:
            if (class_name and child.class_name() == class_name) or (auto_id and child.automation_id() == auto_id) or (not class_name and not auto_id):
                child_list.append(child)  # Add child to the list
            # Recursively list child windows of the current child (if any)
            list_all_children(child)

    list_all_children(window)
    return child_list
def click_object_by_name(window_title, name, control_type):
    try:
        cp_window = Application(backend='uia').connect(title_re=window_title)
        window = cp_window.window(title_re=window_title)
        button_region = window.child_window(title_re=name, control_type=control_type)
        if button_region.exists(timeout=5):
            button_region.click_input()
            sleep(1)
    except Exception as e:
        print(e)
        print(f'button name {name} not found')
        return True
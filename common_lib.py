import codecs
import os
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
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

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

# Function search link
def link_search(link):
    # Đường dẫn tới Edge WebDriver đã tải về
    edge_driver_path = "C:/msedgedriver.exe"

    # Khởi tạo dịch vụ Edge WebDriver
    service = Service(executable_path=edge_driver_path)

    # Cấu hình các tùy chọn cho Edge

    # Danh sách User-Agent
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
        # Thêm nhiều User-Agent khác nếu cần
    ]

    options = webdriver.EdgeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents)}")

    # Khởi tạo trình điều khiển (driver) cho Edge
    driver = webdriver.Edge(service=service, options=options)

    # Mở trang web Google
    driver.get(f"{link}")

    return driver

#Function click by id
def click_by_id(driver, id):
    element = driver.find_element(By.ID, id)
    print('display', element.is_displayed())
    element.click()

#Function click by Xpath
def click_by_xpath(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    print('display', element.is_displayed())
    element.click()
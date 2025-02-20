from time import sleep

from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome driver with Selenium Wire
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Access the website
driver.get('https://bank.shinhan.com/index.jsp#252800000000')

# Wait for the download button to be clickable
wait = WebDriverWait(driver, 30)
download_button = wait.until(EC.element_to_be_clickable((By.ID, 'anc_astxInstalledForWin')))
download_button.click()

print('click')
# Wait for the network request to be made

# Capture the download URL from the network requests
download_url = None
for request in driver.requests:
    print(request.response)
    print(request.url)
    # if request.response and "astxdn.EXE" in request.url:
    #     download_url = request.url
    #     print(f"Download Link: {download_url}")
    #     break

# Close the driver
driver.quit()
href="https:///bandizip/dl.php?web"
https://kr.bandisoft.com/bandizip/dl.php?web
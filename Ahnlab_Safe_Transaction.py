import random
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

from common_lib import link_search, click_by_id, click_by_xpath

driver = link_search('https://www.shinhan.com')

sleep(30)

#Click login btn
click_by_id(driver, 'btn_login')
sleep(25)

# Click login btn
click_by_id(driver, 'install_all')
sleep(15)

click_by_xpath(driver, '//*[@id="install_all"]')
sleep(15)

#Click login btn
click_by_id(driver, 'anc_astxInstalledForWin')
sleep(15)






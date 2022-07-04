from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import cl_vars
import url

local_bin_chromedriver = "/usr/local/bin/chromedriver"
service = Service(executable_path=local_bin_chromedriver)
driver = webdriver.Chrome(service=service)


def get_craigslist(cl_site):
    driver.get(cl_site)
    driver.find_element(By.XPATH, cl_vars.search_box).send_keys(cl_vars.car_to_find + Keys.ENTER)
    driver.find_element(By.XPATH, cl_vars.owner_btn).click()
    driver.find_element(By.XPATH, cl_vars.drp_down).click()
    driver.find_element(By.XPATH, cl_vars.lowest_to_highest).click()




get_craigslist(url.cl_inland_empire_auto_search)

driver.quit()
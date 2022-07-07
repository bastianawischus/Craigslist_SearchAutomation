from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import cl_vars
import url

local_bin_chromedriver = "/usr/local/bin/chromedriver"
service = Service(executable_path=local_bin_chromedriver)
driver = webdriver.Chrome(service=service)

search_result_dict = {}
test_dict = {
    "7497030014":"https://orangecounty.craigslist.org/cto/d/irvine-2005-lexus-gx470/7497030014.html",
    "7504701007":"https://orangecounty.craigslist.org/cto/d/huntington-beach-2006-lexus-gx470/7504701007.html"
}


def get_craigslist(cl_site):
    driver.get(cl_site)
    driver.find_element(By.XPATH, cl_vars.search_box).send_keys(cl_vars.car_to_find + Keys.ENTER)
    driver.find_element(By.XPATH, cl_vars.owner_btn).click()
    driver.find_element(By.XPATH, cl_vars.drp_down).click()
    driver.find_element(By.XPATH, cl_vars.newest_match).click()
    get_data_pids()

def get_data_pids ():
    """ Gets called by the get_craigslist function, finds the search results
    stores all the list elements (li) in a list. Itterates through the
    list and collects all unique PID's and URL to each listing. Lastly adds all
    PID's and URL's to the search_result_dict.

    NOTE: Future improvement - This could return a dictionary which can be
    saved. Then there are multiple dictionaries for each Craigslist location.
    """
    top_search_results = driver.find_element(By.ID, 'search-results')
    single_result = top_search_results.find_elements(By.TAG_NAME, 'li')
    for li_element in single_result:
        pid = li_element.get_attribute('data-pid')
        find_by_pid = li_element.find_element(By.TAG_NAME, 'a')
        pid_url = find_by_pid.get_property('href')
        search_result_dict[pid] = pid_url
        # print(pid, pid_url)
    # print(search_result_dict)

def extract_data_from_URLs():
    #TODO
    # 1 Itterate throught dict
    # 2 Go to URL and capture CL base info
    # 2a condition, cylinders, fuel, odometer,
    #    VIN, title status, paint color, type
    # 2b Add date by days posted - todays date (import date and time)
    #    and add the date in the DB, add area of CL into DB table
    # 2c Add the above info with URL and data pid into the database
    title = ""
    price = ""
    location = ""
    condition = ""
    cylinders = ""
    fuel = ""
    odometer = ""
    vin = ""
    title_status = ""
    paint_color = ""
    engine_type = ""
    for listing in test_dict:
        listing_url = test_dict[listing]
        driver.get(listing_url)
        title = driver.find_element(By.ID, 'titletextonly').text
        price = driver.find_element(By.CLASS_NAME, 'price').text
        location = driver.find_element(By.CSS_SELECTOR, 'small').text
        info_box = driver.find_element(By.XPATH, cl_vars.info_box_xpath)
        info_span_list = info_box.find_elements(By.CSS_SELECTOR, 'span')
        for info_span in info_span_list:
            print(info_span.text)
        print(title, price, location)


# get_craigslist(url.cl_inland_empire_auto_search)
# get_craigslist(url.cl_OC_auto_search)
# print(len(search_result_dict))
# driver.quit()
extract_data_from_URLs()
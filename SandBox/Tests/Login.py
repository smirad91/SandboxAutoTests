import time

from selenium import webdriver

from Lib.functions import open_use_case, get_input, open_use_cases_page

chrome = webdriver.Chrome()
chrome.get("https://qa-sandbox.apps.htec.rs/")

chrome.find_element_by_css_selector("a[href='/login']").click()

time.sleep(3)

chrome.find_element_by_name("email").send_keys("smirad91@gmail.com")
chrome.find_element_by_name("password").send_keys("qasb2020cao$")
chrome.find_element_by_css_selector("button[type='submit']").click()

time.sleep(6)


# chrome.find_element_by_xpath("//*[contains(text(),'{}')]".format("se cases")).click()
open_use_cases_page(chrome)
time.sleep(2)
open_use_case(chrome, "Title")
time.sleep(2)
get_input(chrome)

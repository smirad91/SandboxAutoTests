# Created by <sr>

from selenium import webdriver
from Lib.sandBoxSite.login import LoginPage
from Lib.sandBoxSite.use_cases import UseCasePage
from Models.UseCase import UseCase

### variables (should be in separate json file as key values)
username = "smirad91@gmail.com"
password = "qasb2020cao$"
url = "https://qa-sandbox.apps.htec.rs/"
use_case = UseCase("Use case created by automated test - Delete me", "description",
                "expected result", ["first step"])
### variables end


browser = webdriver.Chrome()
browser.get(url)

login_page = LoginPage(browser)
login_page.login(username, password)
use_case_page = UseCasePage(browser)
use_case_page.open_use_cases_page()

# log.info("Create two use cases with same parameters")
use_case_page.create_use_case()
use_case_page.set_input(use_case)
use_case_page.submit_use_case()

use_case_page.create_use_case()
use_case_page.set_input(use_case)
use_case_page.submit_use_case()

number_of_usecases = use_case_page.number_of_use_case(use_case.title)
if number_of_usecases > 1:
    for i in range(number_of_usecases):
        use_case_page.delete_use_case(use_case.title)
    assert False, "Created multiple use cases with same name"
if number_of_usecases == 0:
    assert False, "Not one use case is created"

browser.close()



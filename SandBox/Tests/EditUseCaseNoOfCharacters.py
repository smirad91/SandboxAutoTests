from selenium import webdriver
from Lib.login import LoginPage
from Lib.use_cases import UseCasePage
from Models.UseCase import UseCase

###variables (should be in separate json file as key values)
username = "smirad91@gmail.com"
password = "qasb2020cao$"
url = "https://qa-sandbox.apps.htec.rs/"
use_case = UseCase("Use Case Created From Automated Test - Delete Me", "Created automatically as precondition",
                     "Expected results automatically created", ["Open some page", "Create list", "Sort created list"])
###variables end



browser = webdriver.Chrome()
browser.get(url)

login_page = LoginPage(browser)
login_page.login(username, password)
use_case_page = UseCasePage(browser)
use_case_page.open_use_cases_page()

###precondition for test is to have use case created for testing purposes
use_case_page.create_use_case()
use_case_page.set_input(use_case)
use_case_page.submit_use_case()
###precondition end

use_case_page.open_use_case(use_case.title)
opened_use_case = use_case_page.get_input()

opened_use_case.edit_on_specific_way()
use_case_page.set_input(opened_use_case)
use_case_page.submit_use_case()


###wrap up test, remove everything that is changed by this test
use_case_page.delete_use_case(opened_use_case.title)
###wrap up end

browser.close()


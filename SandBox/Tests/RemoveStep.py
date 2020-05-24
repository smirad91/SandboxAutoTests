# Created by <sr>

from selenium import webdriver
from Lib.sandBoxSite.login import LoginPage
from Lib.sandBoxSite.use_cases import UseCasePage


### variables (should be in separate json file as key values)
from Models.UseCase import UseCase

username = "smirad91@gmail.com"
password = "qasb2020cao$"
url = "https://qa-sandbox.apps.htec.rs/"
use_case = UseCase("Use case created by automated test - Delete me", "description",
                "expected result", ["first step", "second step", "third step", "fourth step", "fifth step"])
step_to_delete = 2
### variables end


browser = webdriver.Chrome()
browser.get(url)

login_page = LoginPage(browser)
login_page.login(username, password)
use_case_page = UseCasePage(browser)
use_case_page.open_use_cases_page()

### precondition for test is to have use case created for testing purposes
# log.info("Create use case with parameters {}".format(use_case))
use_case_page.create_use_case()
use_case_page.set_input(use_case)
use_case_page.submit_use_case()
### precondition end

# log.info("Delete step {}".format(step_to_delete))
use_case_page.open_use_case(use_case.title)
use_case_page._remove_step(step_to_delete)
use_case_page.submit_use_case()

use_case_page.open_use_case(use_case.title)
edited_use_case = use_case_page.get_input()
# log.screenshot("Steps before deletion")

step = use_case.which_step_deleted(edited_use_case.steps)
if step != use_case.steps[step_to_delete-1]:
    assert False, "Wrong step deleted"
# log.screenshot("Steps after deletion")

use_case_page.go_back()

use_case_page.delete_use_case(use_case.title)

browser.close()


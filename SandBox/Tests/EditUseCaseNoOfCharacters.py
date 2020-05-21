from Lib.common import start_browser, go_to
from Lib.use_cases import login, open_use_cases_page, does_exist_use_case, open_use_case, \
    get_input, set_input, create_use_case, submit_use_case, delete_use_case
from Models.UseCase import UseCase

#variables below should be in separate json file as key values
username = "smirad91@gmail.com"
password = "qasb2020cao$"
url = "https://qa-sandbox.apps.htec.rs/"
# test_case_data = ["Use Case Created From Automated Test - Delete Me", "Created automatically as precondition",
#                     "Expected results automatically created", ["Open some page", "Create list", "Sort created list"]]
use_case = UseCase("Use Case Created From Automated Test - Delete Me", "Created automatically as precondition",
                     "Expected results automatically created", ["Open some page", "Create list", "Sort created list"])

browser = start_browser()
go_to(browser, url)
login(browser, username, password)
open_use_cases_page(browser)

###precondition for test is to have use case created for testing purposes
create_use_case(browser)
set_input(browser, use_case)
submit_use_case(browser)
###precondition end

open_use_case(browser, use_case.title)
opened_use_case = get_input(browser)

opened_use_case.edit_characters()
set_input(browser, opened_use_case)

submit_use_case(browser)


###wrap up test, remove everything that is changed
delete_use_case(browser, opened_use_case.title)
###wrap up end


from SandBox.Lib.functions import start_browser, go_to, login, open_use_cases_page, does_exist_use_case, open_use_case, \
    get_input, set_input, create_use_case

username = "smirad91@gmail.com"
password = "qasb2020cao$"
use_case_title = "Use case for automated test EditUseCaseNoOfCharacters"

browser = start_browser()


go_to(browser, "https://qa-sandbox.apps.htec.rs/")
login(browser, username, password)
open_use_cases_page(browser)
create_use_case(browser)
#
# if does_exist_use_case(browser, use_case_title):
#     open_use_case(browser, use_case_title)
# else:
#     assert False, "Use case {} does not exist".format(use_case_title)

use_case_info = get_input(browser)

set_input(browser, ["fdfdfdfdf", "fdfd", "dsdfsdfds", ["samo jedan step"]])



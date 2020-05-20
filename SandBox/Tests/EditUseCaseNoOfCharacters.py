import time

from SandBox.Lib.functions import start_browser, go_to, login, open_use_cases_page, does_exist_use_case, open_use_case, \
    get_input, set_input, create_use_case, submit_use_case, delete_use_case

username = "smirad91@gmail.com"
password = "qasb2020cao$"
test_case_data = ["fdfdfdfdf", "fdfd", "dsdfsdfds", ["samo jedan step", "dva", "tri"]]


use_case_title = "Use case for automated test EditUseCaseNoOfCharacters"

browser = start_browser()


go_to(browser, "https://qa-sandbox.apps.htec.rs/")
login(browser, username, password)
open_use_cases_page(browser)
create_use_case(browser)
set_input(browser, test_case_data)
submit_use_case(browser)

open_use_case(browser, test_case_data[0])
current_use_case_info = get_input(browser)
browser.find_element_by_css_selector("a[href='/use-cases']").click()
time.sleep(3)
print(current_use_case_info)
for i in range(4):
    if(i==3):
        for b in range(3):
            current_use_case_info[i][b] = "This field previously had {} characters".format(len(current_use_case_info[i][b]))
    else:
        current_use_case_info[i] = "This field previously had {} characters".format(len(current_use_case_info[i]))

open_use_case(browser, test_case_data[0])
set_input(browser, current_use_case_info)

submit_use_case(browser)

delete_use_case(browser, current_use_case_info[0])



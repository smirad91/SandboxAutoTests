import time

from selenium import webdriver


def open_use_case(driver, title):
    useCaseList = driver.find_element_by_class_name("list-group").find_elements_by_tag_name("a")
    for ucl in useCaseList:
        if title.lower() == ucl.text.lower():
            ucl.click()
            break

def does_exist_use_case(driver, title):
    exist = False
    useCaseList = driver.find_element_by_class_name("list-group").find_elements_by_tag_name("a")
    for ucl in useCaseList:
        if title.lower() == ucl.text.lower():
            exist = True
            break
    return exist

def get_input(driver):
    #returns list
    title = driver.find_element_by_name("title").get_attribute('value')
    description = driver.find_element_by_name("description").text
    expected_result = driver.find_element_by_name("expected_result").get_attribute('value')
    # stepParentElement = driver.find_element_by_css_selector("form[autocomplete='']")
    steps = driver.find_elements_by_css_selector("input[placeholder*='* Use case step']")
    print(title)
    print(description)
    print(expected_result)
    for s in steps:
        print(s.get_attribute('value'))
    return [title, description, expected_result, steps]

def set_input(driver, input_list):
    wait_until(lambda:driver.find_element_by_name("title"), 10)
    driver.find_element_by_name("title").send_keys(input_list[0])
    driver.find_element_by_name("description").send_keys(input_list[1])
    driver.find_element_by_name("expected_result").send_keys(input_list[2])
    steps = driver.find_elements_by_css_selector("input[placeholder*='* Use case step']")
    for i, step in enumerate(input_list[3]):
        steps[i].send_keys(step)

def input_use_case_info(driver, title, dsc, er, steps):
    driver.find_element_by_name("title").send_keys(title)
    driver.find_element_by_name("description").text = dsc
    driver.find_element_by_name("expected_result").send_keys(er)
    driver.find_element_by_css_selector("input[placeholder*='* Use case step']").send_keys["gfg"]
    for step in steps:
        pass

def create_use_case(driver):
    driver.find_element_by_css_selector("a[data-testid='create_use_case_btn']").click()

def open_use_cases_page(driver):
    driver.find_element_by_xpath("//*[contains(text(),'{}')]".format("se cases")).click()

def login(driver, username, password):
    try:
        wait_until(lambda: driver.find_element_by_css_selector("a[href='/login']"), 10)
        driver.find_element_by_css_selector("a[href='/login']").click()
    except Exception as ex:
        # Log(ex.message)
        pass

    wait_until(lambda: driver.find_element_by_name("email"), 10)
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button[type='submit']").click()
    wait_until(lambda: len(driver.find_elements_by_css_selector("button[type='submit']"))==0, 10)

def start_browser():
    chrome = webdriver.Chrome()
    return chrome

def go_to(driver, url):
    driver.get(url)

def wait_until(somepredicate, timeout, period=1, errorMessage="Timeout expired"):
    """
    Somepredicate is function that returns True or False. This function is executed every for period during
    timeout. When somepredicate return True wait is done. If somepredicate don't return True during timeout,
    exception is raised.

    :param somepredicate: Function that return True of False
    :type somepredicate: func
    :param timeout: Timeout to wait
    :type timeout: int
    :param period: Execute function for every period seconds
    :type period: float
    :return:
    """
    mustend = time.time() + timeout
    value = False
    while time.time() < mustend:
        try:
            value = somepredicate()
        except:
            pass
        if value:
            return True
        time.sleep(period)
    raise Exception(errorMessage)

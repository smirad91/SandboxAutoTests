import time

from selenium import webdriver


def open_use_case(driver, title):
    wait_until(lambda: driver.find_element_by_class_name("list-group"),10)
    print(title)
    print("title je iznad")
    useCaseList = driver.find_element_by_css_selector("div[class*='list-group']").find_elements_by_tag_name("a")
    for ucl in useCaseList:
        if title.lower() == ucl.text.lower():
            ucl.click()
            print("otvori use case")
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
    wait_until(lambda: driver.find_element_by_name("title"), 10)
    title = driver.find_element_by_name("title").get_attribute('value')
    description = driver.find_element_by_name("description").text
    expected_result = driver.find_element_by_name("expected_result").get_attribute('value')
    # stepParentElement = driver.find_element_by_css_selector("form[autocomplete='']")
    steps = driver.find_elements_by_css_selector("input[placeholder*='* Use case step']")
    steps_list = []
    print(title)
    print(description)
    print(expected_result)
    for s in steps:
        steps_list.append(s.get_attribute("value"))
        print(s.get_attribute('value'))
    return [title, description, expected_result, steps_list]

def set_input(driver, input_list):
    wait_until(lambda: driver.find_element_by_name("title"), 10)
    driver.find_element_by_name("title").clear()
    driver.find_element_by_name("title").send_keys(input_list[0])
    driver.find_element_by_name("description").clear()
    driver.find_element_by_name("description").send_keys(input_list[1])
    driver.find_element_by_name("expected_result").clear()
    driver.find_element_by_name("expected_result").send_keys(input_list[2])
    steps = driver.find_elements_by_css_selector("input[placeholder*='* Use case step']")
    if len(steps) < len(input_list[3]):
        #click on add step
        add_number = len(input_list[3]) - len(steps)
        add_step_btn = driver.find_element_by_class_name("addTestStep")
        for i in range(add_number):
            time.sleep(1)
            add_step_btn.click()
    elif len(steps) > len(input_list[3]):
        #remove
        remove_number = len(steps) - len(input_list[3])
        remove_btns = driver.find_elements_by_css_selector("button[data-testid='delete_usecase_step_btn']")
        for i in range(remove_number):
            time.sleep(1)
            remove_btns[i].click()
    steps = driver.find_elements_by_css_selector("input[placeholder*='* Use case step']")
    for i, step in enumerate(input_list[3]):
        steps[i].clear()
        steps[i].send_keys(step)

def delete_use_case(driver, title):
    open_use_case(driver, title)
    time.sleep(2)
    driver.find_element_by_css_selector("button[aria-label='delete-button']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()='Delete']").click()
    wait_until(lambda: driver.find_element_by_class_name("list-group"),10)


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

def submit_use_case(driver):
    driver.find_element_by_css_selector("button[type='submit']").click()

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

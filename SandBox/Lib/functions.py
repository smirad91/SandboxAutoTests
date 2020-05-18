def open_use_case(driver, title):
    useCaseList = driver.find_element_by_class_name("list-group").find_elements_by_tag_name("a")
    for ucl in useCaseList:
        if title.lower() == ucl.text.lower():
            ucl.click()
            break

def does_exist(driver, title):
    exist= False
    useCaseList = driver.find_element_by_class_name("list-group").find_elements_by_tag_name("a")
    for ucl in useCaseList:
        if title.lower() == ucl.text.lower():
            exist=True
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




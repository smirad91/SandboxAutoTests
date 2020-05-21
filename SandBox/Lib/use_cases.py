import time
from Lib.common import wait_until
from Models.UseCase import UseCase

class UseCasePage:

    def __init__(self, browser):
        self.browser = browser

    def open_use_case(self, title):
        """
        From use cases page opens use case with given title
        :param driver: webdriver used for browser starting
        """
        wait_until(lambda: self.browser.find_element_by_class_name("list-group"),10)
        print(title)
        print("title je iznad")
        useCaseList = self.browser.find_element_by_css_selector("div[class*='list-group']").find_elements_by_tag_name("a")
        for ucl in useCaseList:
            if title.lower() == ucl.text.lower():
                ucl.click()
                print("otvori use case")
                break


    def does_exist_use_case(self, title):
        """
        Checks if use case with given title exists
        :param driver: webdriver used for browser starting
        """
        exist = False
        wait_until(lambda: self.browser.find_element_by_class_name("list-group"), 10)
        useCaseList = self.browser.find_element_by_class_name("list-group").find_elements_by_tag_name("a")
        for ucl in useCaseList:
            if title.lower() == ucl.text.lower():
                exist = True
                break
        return exist

    def get_input(self):
        #returns list
        wait_until(lambda: self.browser.find_element_by_name("title"), 10)
        title = self.browser.find_element_by_name("title").get_attribute('value')
        description = self.browser.find_element_by_name("description").text
        expected_result = self.browser.find_element_by_name("expected_result").get_attribute('value')
        # stepParentElement = driver.find_element_by_css_selector("form[autocomplete='']")
        steps = self.browser.find_elements_by_css_selector("input[placeholder*='* Use case step']")
        steps_list = []
        print(title)
        print(description)
        print(expected_result)
        for s in steps:
            steps_list.append(s.get_attribute("value"))
            print(s.get_attribute('value'))
        return UseCase(title, description, expected_result, steps_list)

    def set_input(self, use_case):
        wait_until(lambda: self.browser.find_element_by_name("title"), 10)
        self.browser.find_element_by_name("title").clear()
        self.browser.find_element_by_name("title").send_keys(use_case.title)
        self.browser.find_element_by_name("description").clear()
        self.browser.find_element_by_name("description").send_keys(use_case.description)
        self.browser.find_element_by_name("expected_result").clear()
        self.browser.find_element_by_name("expected_result").send_keys(use_case.expected_result)
        steps = self.browser.find_elements_by_css_selector("input[placeholder*='* Use case step']")
        if len(steps) < len(use_case.steps):
            #click on add step
            add_number = len(use_case.steps) - len(steps)
            add_step_btn = self.browser.find_element_by_class_name("addTestStep")
            for i in range(add_number):
                time.sleep(1)
                add_step_btn.click()
        elif len(steps) > len(use_case.steps):
            #remove
            remove_number = len(steps) - len(use_case.steps)
            remove_btns = self.browser.find_elements_by_css_selector("button[data-testid='delete_usecase_step_btn']")
            for i in range(remove_number):
                time.sleep(1)
                remove_btns[i].click()
        steps = self.browser.find_elements_by_css_selector("input[placeholder*='* Use case step']")
        for i, step in enumerate(use_case.steps):
            steps[i].clear()
            steps[i].send_keys(step)

    def delete_use_case(self, title):
        if self.does_exist_use_case(title):
            print("Warning: Use case {} already exists".format(title))
        self.open_use_case(title)
        time.sleep(2)
        self.browser.find_element_by_css_selector("button[aria-label='delete-button']").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//button[text()='Delete']").click()
        wait_until(lambda: self.browser.find_element_by_class_name("list-group"),10)


    def input_use_case_info(self, title, dsc, er, steps):
        self.browser.find_element_by_name("title").send_keys(title)
        self.browser.find_element_by_name("description").text = dsc
        self.browser.find_element_by_name("expected_result").send_keys(er)
        self.browser.find_element_by_css_selector("input[placeholder*='* Use case step']").send_keys["gfg"]
        for step in steps:
            pass

    def create_use_case(self):
        self.browser.find_element_by_css_selector("a[data-testid='create_use_case_btn']").click()

    def open_use_cases_page(self):
        self.browser.find_element_by_xpath("//*[contains(text(),'{}')]".format("se cases")).click()

    def submit_use_case(self):
        self.browser.find_element_by_css_selector("button[type='submit']").click()




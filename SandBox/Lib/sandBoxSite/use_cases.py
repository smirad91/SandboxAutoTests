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
        # log.info("Open use case: {}".format(title))
        wait_until(lambda: self.browser.find_element_by_class_name("list-group"), 10)
        use_case_list = self.browser.find_element_by_css_selector("div[class*='list-group']")\
            .find_elements_by_tag_name("a")
        for ucl in use_case_list:
            if title.lower() == ucl.text.lower():
                ucl.click()
                wait_until(lambda: self.browser.find_element_by_xpath("//*[contains(text(), 'Edit Use Case')]"), 10)
                # log.screenshot("Use case opened")
                return True
        # log.info("Use case {} does not exist".format(title))
        return False

    def number_of_use_case(self, title):
        number = 0
        wait_until(lambda: self.browser.find_element_by_class_name("list-group"), 10)
        use_case_list = self.browser.find_element_by_css_selector("div[class*='list-group']") \
            .find_elements_by_tag_name("a")
        for ucl in use_case_list:
            if title.lower() == ucl.text.lower():
                number += 1
        return number


    def get_input(self):
        """
        From opened use case inputs, creates UseCase object
        :return: All input fields from opened use case
        :type: UseCase
        """
        # log.info("Get input from opened use case")
        wait_until(lambda: self.browser.find_element_by_name("title"), 10)
        title = self.browser.find_element_by_name("title").get_attribute('value')
        description = self.browser.find_element_by_name("description").text
        expected_result = self.browser.find_element_by_name("expected_result").get_attribute('value')
        steps = self.browser.find_elements_by_css_selector("input[placeholder*='* Use case step']")
        steps_list = []
        for s in steps:
            steps_list.append(s.get_attribute("value"))
        use_case = UseCase(title, description, expected_result, steps_list)
        # log.screenshot(use_case)
        return use_case

    def set_input(self, use_case):
        """
        On opened use case insert input
        :param use_case: Contains input data to insert
        :type: UseCase
        """
        # log.info("Set input in use case {}".format(use_case))
        wait_until(lambda: self.browser.find_element_by_name("title"), 10)
        self.browser.find_element_by_name("title").clear()
        self.browser.find_element_by_name("title").send_keys(use_case.title)
        self.browser.find_element_by_name("description").clear()
        self.browser.find_element_by_name("description").send_keys(use_case.description)
        self.browser.find_element_by_name("expected_result").clear()
        self.browser.find_element_by_name("expected_result").send_keys(use_case.expected_result)
        steps = self.browser.find_elements_by_css_selector("input[placeholder*='* Use case step']")
        if len(steps) < len(use_case.steps):
            add_number = len(use_case.steps) - len(steps)
            self._add_step(add_number)
        elif len(steps) > len(use_case.steps):
            remove_number = len(steps) - len(use_case.steps)
            for i in range(remove_number):
                self._remove_step(i)
        # log.screenshot("Number of steps set. Number is: {}".format(len(use_case.steps)))
        self._input_steps(use_case.steps)

    def _input_steps(self, steps_description):
        # log.info("Insert steps description")
        steps = self.browser.find_elements_by_css_selector("input[placeholder*='* Use case step']")
        for i, step in enumerate(steps_description):
            steps[i].clear()
            steps[i].send_keys(step)
        # log.screenshot("Step description inserted")

    def _add_step(self, number):
        # log.info("Add {} steps".format(number))
        add_step_btn = self.browser.find_element_by_class_name("addTestStep")
        for i in range(number):
            time.sleep(1)
            add_step_btn.click()

    def _remove_step(self, serial_number):
        # log.info("Remove {} step".format(serial_number))
        serial_number = serial_number - 2
        remove_btns = self.browser.find_elements_by_css_selector("button[data-testid='delete_usecase_step_btn']")
        remove_btns[serial_number].click()

    def delete_use_case(self, title):
        """
        Deletes use case with given title
        """
        # log.info("Delete use case {}".format(title))
        if self.open_use_case(title):
            time.sleep(2)
            self.browser.find_element_by_css_selector("button[aria-label='delete-button']").click()
            time.sleep(2)
            self.browser.find_element_by_xpath("//button[text()='Delete']").click()
            wait_until(lambda: self.browser.find_element_by_class_name("list-group"),10)
            # log.screenshot("Use case is deleted")
        else:
            assert False, "Use case does not exist"
            pass

    def create_use_case(self):
        """
        Click on button for create use case
        """
        # log.info("Click on create use case button")
        wait_until(lambda: self.browser.find_element_by_css_selector("a[data-testid='create_use_case_btn']"), 10)
        self.browser.find_element_by_css_selector("a[data-testid='create_use_case_btn']").click()
        wait_until(lambda: self.browser.find_element_by_xpath("//*[contains(text(), 'New Use Case')]"), 10)
        # log.screenshot("New use case form opened")

    def open_use_cases_page(self):
        """
        From dashboard opens use case page
        """
        # log.info(Open use cases page)
        wait_until(lambda: self.browser.find_element_by_xpath("//*[contains(text(),'{}')]".format("se cases")), 10)
        self.browser.find_element_by_xpath("//*[contains(text(),'{}')]".format("se cases")).click()
        wait_until(lambda: self.browser.find_element_by_css_selector("a[data-testid='create_use_case_btn'"), 10)
        # log.screenshot("Use cases page opened")

    def go_back(self):
        # log.info("Go back to use cases page")
        wait_until(lambda: self.browser.find_element_by_css_selector("a[href='/use-cases']"), 10)
        self.browser.find_element_by_css_selector("a[href='/use-cases']").click()
        wait_until(lambda: "//b[text()='Use Cases']", 10)
        time.sleep(1) # this waiting is added because test fails if this line does not exist for some reason

    def submit_use_case(self):
        """
        Click on submit on create use case page
        """
        # log.info("Click on submit use case")
        wait_until(lambda: self.browser.find_element_by_css_selector("button[type='submit']"), 10)
        self.browser.find_element_by_css_selector("button[type='submit']").click()
        wait_until(lambda: self.browser.find_element_by_css_selector("a[data-testid='create_use_case_btn']"), 10)
        # log.screenshot("Clicked on submit. Use cases page is opened now.")




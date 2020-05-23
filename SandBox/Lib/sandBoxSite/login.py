from Lib.common import wait_until


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        """
        Login with given username and password
        """
        # <log.info("Open login page")>
        wait_until(lambda: self.browser.find_element_by_css_selector("a[href='/login']"), 10)
        self.browser.find_element_by_css_selector("a[href='/login']").click()
        wait_until(lambda: self.browser.find_element_by_name("email"), 10)
        #<log.screenshot("Login page is opened. Insert {0} and {1}".format(username, password))>
        self.browser.find_element_by_name("email").send_keys(username)
        self.browser.find_element_by_name("password").send_keys(password)
        self.browser.find_element_by_css_selector("button[type='submit']").click()
        wait_until(lambda: len(self.browser.find_elements_by_css_selector("button[type='submit']")) == 0, 10)
        #<log.screenshot("Logged in")>
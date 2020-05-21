import time

from selenium import webdriver


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

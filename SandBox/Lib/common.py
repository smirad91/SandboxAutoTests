import time


def wait_until(somepredicate, timeout=60, period=1, errorMessage="Timeout expired"):
    """
    Parameter somepredicate is function that returns True or False. This function is executed for every period during
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

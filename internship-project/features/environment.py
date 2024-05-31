from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from support.logger import logger
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    ###CHROME
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ### BROWSER WITH DRIVERS:
    ###FIREFOX
    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service)

    ###EDGE
    # service = Service(executable_path=r'C:\Users\leoh2\internship-project\internship-project\msedgedriver.exe')
    # context.driver = webdriver.Edge(service=service)

    ###HEADLESS MODE###
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument("--window-size=1920,1080")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(options=options, service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(6)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info('Started step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        # logger.info('Step failed', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

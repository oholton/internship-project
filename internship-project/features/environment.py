from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from support.logger import logger
from app.application import Application


#to run Behave Allure
#behave -f allure_behave.formatter:AllureFormatter -o test_results ./features/tests/filter_search.feature
#allure serve ./test_results/



def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    ###CHROME
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ###MOBILE TESTING###

    # if 'mobile' in scenario_name.lower():
    #     mobile_emulation = {"deviceName": "Nexus 5"}
    #     chrome_options = Options()
    #     chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #     service = Service(ChromeDriverManager().install())
    #     context.driver = webdriver.Chrome(service=service, options=chrome_options)
    # else:
    #     driver_path = ChromeDriverManager().install()
    #     service = Service(driver_path)
    #     context.driver = webdriver.Chrome(service=service)

    ### BROWSER WITH DRIVERS:
    ###FIREFOX
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(service=service)

    ###EDGE
    # service = Service(executable_path=r'C:\Users\leoh2\internship-project\internship-project\msedgedriver.exe')
    # context.driver = webdriver.Edge(service=service)

    ###HEADLESS MODE###
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument("--window-size=1920,1080")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(options=options, service=service)

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from http://www.browserstack.com/accounts/settings
    # bs_user = 'oscarholton_d7givp'
    # bs_key = 'cUP1rygoqb4yrH2KDkLV'
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Monterey',
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)



    context.driver.maximize_window()
    context.driver.implicitly_wait(8)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


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

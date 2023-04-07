"""
Environment for Behave Testing
"""
from os import getenv
from selenium import webdriver

WAIT_SECONDS = int(getenv('WAIT_SECONDS', '60'))
BASE_URL = getenv('BASE_URL', 'http://localhost:8080')


def before_all(context):
    """ Executed once before all tests """
    context.BASE_URL = BASE_URL
    context.WAIT_SECONDS = WAIT_SECONDS
    # Setup Chrome webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(context.WAIT_SECONDS)  # seconds
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini"
    context.config.setup_logging()


def after_all(context):
    """ Executed after all tests """
    context.driver.quit()

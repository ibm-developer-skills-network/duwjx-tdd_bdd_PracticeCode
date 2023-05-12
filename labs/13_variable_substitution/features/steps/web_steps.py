# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Web Steps
Steps file for web interactions with Selenium
For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""

from behave import given, when, then

@given('I am on the "Home Page"')
def step_impl(context):
    context.response = context.driver.get(context.base_url)

@when('I set the "Category" to "dog"')
def step_impl(context):
    element = context.driver.find_element_by_id('pet_category')
    element.clear()
    element.send_keys('dog')

@when('I click the "Search" button')
def step_impl(context):
    element = context.driver.find_element_by_id('search-btn')
    element.click()

@then('I should see the message "Success"')
def step_impl(context):
    element = context.driver.find_element_by_id('flash_message')
    assert "Success" in element.text

@then('I should see "Fido" in the results')
def step_impl(context):
    element = context.driver.find_element_by_id('search_results')
    assert "Fido" in element.text

@then('I should not see "Kitty" in the results')
def step_impl(context):
    element = context.driver.find_element_by_id('search_results')
    assert "Kitty" not in element.text

@then('I should not see "Leo" in the results')
def step_impl(context):
    element = context.driver.find_element_by_id('search_results')
    assert "Leo" not in element.text

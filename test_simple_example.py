import pytest


import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

""" @pytest.fixture(scope="module")
under this module the scope will run only ones 
"""

"""@pytest.fixture(scope="function")
this one is default 
it means ech one of the function will run fixture whenever will colling that and will be destroyed after ech functions
will be executed
"""

"""@pytest.fixture(scope="class")
its means this fixture will be limited to the scope of this class 
"""

"""@pytest.fixture(scope="package")
its means this fixture will be limited to the package currently in
"""

"""@pytest.fixture(scope="session")
its means under the executions under the full session the fixture will be executed only ones for all of the test
"""
# @pytest.fixture(scope="session")
@pytest.fixture()
def init_web_driver(request):
    print("\n In web driver init")

    # it will be just return
    # return webdriver.Chrome()

    # so after returning also will continue the code
    # yield webdriver.Chrome()


    driver: WebDriver
    browser_name = request.config.option.browser_name

    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    yield driver
    print("\n I'm after the yield")
    driver.close()


@pytest.fixture()
def second_fixture():
    print("\n I'm inside the second fixture")



@pytest.mark.system
@pytest.mark.sanity
@pytest.mark.usefixtures("init_web_driver")
def test_my_first_one():
    print("\n i'm inside my first test!")
    my_validation = True
    # raise Exception
    assert my_validation, "The validation of this test has failed!"


def test_my_second_one(init_web_driver, second_fixture):
    driver: WebDriver = init_web_driver
    expected_url = "https://rainthedog.com/"
    driver.get(expected_url)
    actual_url = driver.current_url
    assert expected_url == actual_url, "Expected url didn't match the actual"

    # Pre-conditions
    # Test body
    # Validation / Expected result

import pytest


import pytest
from selenium import webdriver


@pytest.fixture
def init_web_driver():
    print("\n In web driver init")

    return webdriver.Chrome()

@pytest.fixture()
def second_fixture():
    print("\n I'm inside the second fixture")



@pytest.mark.system
@pytest.mark.sanity
@pytest.mark.usefixtures("init_web_driver")
def test_my_first_one():
    print("\n i'm inside my first test!")
    my_validation = True
    assert my_validation, "The validation of this test has failed!"


def test_my_second_one(init_web_driver, second_fixture):
    driver = init_web_driver
    driver.get("http://www.rainthedog.com")
    print("\n i'm inside my second test!")

    # Pre-conditions
    # Test body
    # Validation / Expected result

import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="default name")
def pytest_runtest_setup(item):
    print("\n I'm inside the test setup!")


def pytest_runtest_call(item):
    print("\n I'm inside the test call!")



def pytest_runtest_teardown(item, nextitem):
    print("\n I'm inside the test teardown!")



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    print("\n I'm make report")
    outcome = yield
    rep = outcome.get_result()
    rep.when

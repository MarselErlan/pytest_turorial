import pytest


@pytest.mark.system
@pytest.mark.sanity
def test_my_first_one():
    print("\n i'm inside my first test!")
    my_validation = True
    assert my_validation, "The validation of this test has failed!"


def test_my_second_one():
    print("\n i'm inside my second test!")
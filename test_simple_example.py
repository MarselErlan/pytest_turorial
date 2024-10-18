import pytest


@pytest.mark.sanity
def test_my_first_one():
    print("\n i'm inside my first test!")


def test_my_second_one():
    print("\n i'm inside my second test!")
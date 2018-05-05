import pytest


def reverse(string):
    return string[::-1]

def test_reverse():
    string = "good"
    assert reverse(string) == "doog"

    an_string = "itest"
    assert reverse(an_string) == "testi"

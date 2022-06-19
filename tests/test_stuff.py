import pytest

class MyChosenClass:
    def __init__(self, some_member):
        self.some_member = some_member


@pytest.mark.my_custom_marker(
    MyChosenClass("My info for test a")
)
def test_do_something_a(my_runner):
    print("[myprint]\trunning test_do_something_a")
    print("[myprint]\tHere I will verify the result of my_custom_marker")
    
    
@pytest.mark.my_custom_marker(
    MyChosenClass("My info for test b")
)
def test_do_something_b(my_runner):
    print("[myprint]\trunning test_do_something_b")
    print("[myprint]\tHere I will verify the result of my_custom_marker")


def test_not_supposed_to_run(my_runner):
    print("running test_not_supposed_to_run")

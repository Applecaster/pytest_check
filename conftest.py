import pytest

def pytest_sessionstart(session):
    print("\n[myprint] doing session start stuff\n")


def pytest_sessionfinish(session, exitstatus):
    print("\n[myprint] doing teardown stuff\n")


def pytest_collection_finish(session):
    print("\n[myprint] Preprocessing collected tests...\n")
    
    tests_to_run = session.items
    for test_obj in tests_to_run:
        for stuff_to_do in test_obj.iter_markers(name='my_custom_marker'):
            print(f"[myprint]\t-Test '{test_obj.name}' to be run:")
            print(f"[myprint]\t\t-Contains object {str(stuff_to_do.args[0])}")
            print(f"[myprint]\t\t-With info '{stuff_to_do.args[0].some_member}'")
            
    print("\n[myprint] Finished preprocessing the tests. Ready to start running...\n")


@pytest.fixture(autouse=True)
def my_runner():
    print("\n[myprint] runner fixture initializes before test case")
    yield
    print("\n[myprint] runner fixture dies after test case\n")


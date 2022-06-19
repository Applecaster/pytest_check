import pytest

def pytest_sessionstart(session):
    print("doing session start stuff")

def pytest_sessionfinish(session, exitstatus):
    print("doing teardown stuff")
    


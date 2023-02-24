import pytest


@pytest.fixture(autouse=True)
def crear_file():
    """Clear data in file"""
    with open('testfile.txt', 'w'):
        pass
import os
import pytest

def get_py_files(path):
    py_files = []
    for r, d, f in os.walk(path):
        for file in f:
            if ('.py' in file) and (r == 'my_funcs'):
                
                py_files.append((r, file))
    return py_files

all_files = get_py_files('my_funcs')
@pytest.mark.parametrize('r, file', all_files)
def test_find_import(r, file):
    """Check for noncorrect import

    Args:
        r (str): directiory
        file (str): file name
    """
    with open(f'{r}/{file}', 'r') as file_text:
        read_file = file_text.read()
        
    assert 'import *'  not in read_file, 'Не правильно импортирован модуль'
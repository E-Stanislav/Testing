from my_funcs.file_reader import read_from_file

def create_data(test_data):
    with open('testfile.txt', 'a') as file:
        file.writelines(test_data)

def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three']
    create_data(test_data)
    assert read_from_file('testfile.txt') == test_data
    

def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n']
    create_data(test_data)
    assert read_from_file('testfile.txt') == test_data
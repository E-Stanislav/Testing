def read_from_file(filepath):
    with open(filepath, 'r') as file:
        return file.readlines()
    

print(read_from_file('my_funcs/prodfile.txt'))
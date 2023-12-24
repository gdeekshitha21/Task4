def read_files(file_name):
    try:
        with open(file_name,'r')as file:
            content=file.read()
            print(content)
    except FileNotFoundError:
        print("oops! the file'{}' does not exist.".format(file_name))   
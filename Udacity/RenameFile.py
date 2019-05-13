import os


def rename_file():
    file_list = os.listdir("/Users/nayakhil/downloads/prank")
    cwd = os.getcwd()
    os.chdir("/Users/nayakhil/downloads/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(cwd)
    file_list = os.listdir("/Users/nayakhil/downloads/prank")
    print(file_list)

rename_file()
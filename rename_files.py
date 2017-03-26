import os

def rename_files():
    files_list = os.listdir(r"E:\Workspace\Python\prank")

    saved_path = os.getcwd()

    print("Working in"+saved_path)

    os.chdir(r"E:\Workspace\Python\prank")

    for files_name in files_list:
        print("Old Name -"+files_name)
        print("New Name -"+files_name.translate(str.maketrans('','','0123456789')))

        os.rename(files_name, files_name.translate(str.maketrans('','','0123456789')))

    os.chdir(saved_path)


rename_files()

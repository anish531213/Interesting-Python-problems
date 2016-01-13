import os
def rename_files():
    file_list = os.listdir("/home/anish/Documents/prank")
    print(file_list)
    cur_dir = os.getcwd()
    os.chdir("/home/anish/Documents/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789")
    os.chdir(cur_dir)
    

    
rename_files()
                  




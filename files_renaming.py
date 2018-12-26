import os
def rename_files():
    file_list = os.listdir("/Users/alexeidudarev/Downloads/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("currenr directory is :" + saved_path)
    os.chdir("/Users/alexeidudarev/Downloads/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans('','','1234567890')))
    os.chdir(saved_path)
                  
rename_files()    

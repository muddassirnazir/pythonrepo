import os
import string
def rename_files():
        file_list = os.listdir(r"C:\Users\muddassir.nazir\Desktop\Udacity_Python\prank")
        print (file_list)
        saved_path = os.getcwd()
        print ("Current working directory is" +saved_path)
        os.chdir(r"C:\Users\muddassir.nazir\Desktop\Udacity_Python\prank")
        for file_name in file_list:
            os.rename(file_name, file_name.translate(str.maketrans("","",string.digits)))
rename_files()

import os

home_path = os.getenv("HOME")
os.chdir(home_path)
print("1: ", os.getcwd())
for content in os.listdir(os.getcwd()):
    if(os.path.isdir(content) and (not content.startswith("."))): #if the content of home dir is a another directory but not hidden
        os.chdir(os.abspath(content))
        for file in os.listdir(os.getcwd()):
            if(os.path.isfile(file) and (file.endswith(".py") or file.endswith(".png") or file.endswith(".txt"))):
                os.remove(os.abspath(file))
        os.chdir("..") #go back
    #   os.chdir(content)
    #   #print(os.getcwd())
    #   for file in os.getcwd():
    #     print(file)
    #     print(type(file))   
    #   os.chdir("..")
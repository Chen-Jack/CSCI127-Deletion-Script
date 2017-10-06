import os

home_path = os.getenv("HOME")

scriptlocation = os.path.abspath("removepy.py") #The location of my remove script

#Creating a hidden folder in home directory and copying the script into it.
os.chdir(home_path)
os.mkdir(".127pythonscript")
os.chdir(".127pythonscript")
os.system("sudo cp "+scriptlocation+" "+os.getcwd())

#create and insert alias into .bashrc
new_alias = ' alias removepy="cd; cd .127pythonscript; python3 removepy.py; cd;" '

os.chdir(home_path)
alias_file = ".bash_aliases"
if not alias_file.exists():
  print("Creating new alias file.")
  os.mkfile(alias_file)

print("Creating alias")  
bash_file = open(alias_file,'a') #Gotta open in append mode yo, otherwise we in trouble
bash_file.write("\n")
bash_file.write("#Alias for running a python deletion script for csci127 at Hunter College.\n")
bash_file.write(new_alias)
bash_file.close()

print("Done. Please close the terminal. You may use the script through the terminal command 'removepy'.")

import os

home_path = os.getenv("HOME")

scriptlocation = os.path.abspath("removepy.py") #The location of my remove script
taglocation = os.path.abspath(".target_tags")   #The location of my tag list

#Creating a hidden folder in home directory and copying the script into it.
os.chdir(home_path)
os.mkdir(".127pythonscript")
os.chdir(".127pythonscript")
os.system("cp "+scriptlocation+" "+os.getcwd())
os.system("cp "+taglocation+" "+os.getcwd())


#Conditionally create .bash_aliases file
os.chdir(home_path)
alias_file = ".bash_aliases"
if alias_file not in os.listdir(os.getcwd()):
  print("Creating new alias file.")
  os.system("touch .bash_aliases")

#Creating an alias
new_alias = 'alias removefiles="cd; cd .127pythonscript; python3 removepy.py; cd;"'

print("Creating alias")  
bash_file = open(alias_file,'a') 
bash_file.write("\n")
bash_file.write("#Alias for running a python deletion script for csci127 at Hunter College.\n")
bash_file.write(new_alias)
bash_file.close()

#Done
print("Done. Please close the terminal")
print("You may use the script through the terminal command 'removepy'.")

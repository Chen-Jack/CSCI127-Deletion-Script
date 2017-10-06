import os

print("Deleting Python files...")

def removefiles(item,tag_list):
  for tag in tag_list:
    if(item.endswith(tag)):
      os.remove(item)
    
home_path = os.getenv("HOME")
os.chdir(home_path)

target_tags = [".py", ".png", ".txt"]

#Delete target files in home directory
for item in os.listdir(os.getcwd()):
  if os.path.isfile(item) and (not item.startswith(".")):
    removefiles(item, target_tags)

#Delete target files 1 level in from home.
for content in os.listdir(os.getcwd()):
  if os.path.isdir(content) and (not content.startswith(".")): #dont check hidden directories
    os.chdir(os.path.abspath(content))	#Go down 1 level
    for item in os.listdir(os.getcwd()):
      if os.path.isfile(item) and (not item.startswith(".")):
        removefiles(item, target_tags)
    os.chdir("..") # go back up 1 level(home)

os.chdir("Desktop") #Delete evreything in desktop
for item in os.listdir(os.getcwd()):
  if(os.path.isfile(item)):
    os.remove(item)
  elif(os.path.isdir(item)):
    os.rmdir(item)
os.chdir(home_path)

os.chdir("Downloads")
for item in os.listdir(os.getcwd()):
  if(os.path.isfile(item)):
    os.remove(item)
  elif(os.path.isdir(item)):
    os.rmdir(item)
os.chdir(home_path)

os.chdir("Documents")
for item in os.listdir(os.getcwd()):
  if(os.path.isfile(item)):
    os.remove(item)
  elif(os.path.isdir(item)):
    os.rmdir(item)
os.chdir(home_path)

print("Done.")




	





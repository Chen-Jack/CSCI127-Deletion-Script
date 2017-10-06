import os
import sys

script_loc = os.getcwd()  #The "home" directory in respect to the location of this script
tag_path = script_loc+"/.target_tags"  #This is the path to my hidden file ".target_tags"

def removefiles(item,tag_list):
  for tag in tag_list:
    if(item.endswith(tag)):
      os.remove(item)
      

if(len(sys.argv) == 1):   #no arguments
  print("Deleting Python files...")

  home_path = os.getenv("HOME")
  os.chdir(home_path)					#LOCATION == HOME

  target_file = open(tag_path)
  target_tags = (target_file.readline()).split()
  target_file.close()

  #Delete target files in home directory
  for item in os.listdir(home_path):
    if os.path.isfile(item) and (not item.startswith(".")): #don't delete hidden files
      removefiles(item, target_tags)

  #Delete target files 1 level down from home.
  for content in os.listdir(home_path): 
    if os.path.isdir(content) and (not content.startswith(".")): #dont check hidden directories
      os.chdir(os.path.abspath(content))	#Go down 1 level
      for item in os.listdir(os.getcwd()):
        if os.path.isfile(item) and (not item.startswith(".")): #don't delete hidden files
          removefiles(item, target_tags)
      os.chdir("..") # go back up 1 level(home)

  os.chdir("Desktop") #Delete everything in desktop
  for item in os.listdir(os.getcwd()):
    if(os.path.isfile(item)):
      os.remove(item)
    #elif(os.path.isdir(item)):
      #os.rmdir(item)
  os.chdir(home_path)

  os.chdir("Downloads") #Delete everything in downloads
  for item in os.listdir(os.getcwd()):
    if(os.path.isfile(item)):
      os.remove(item)
    #elif(os.path.isdir(item)):
      #os.rmdir(item)
  os.chdir(home_path)

  os.chdir("Documents") #Delete everything in documents
  for item in os.listdir(os.getcwd()):
    if(os.path.isfile(item)):
      os.remove(item)
    #elif(os.path.isdir(item)):
     # os.rmdir(item)
  os.chdir(home_path)

  print("Done.")  #Done deleting the files.
    
elif(len(sys.argv) == 2):
  if(sys.argv[1] == "-show"):
    current_flag_file = open(tag_path)
    current_flags = (current_flag_file.readline()).split()
    print("Current Targets:")
    for flag in current_flags:
      print(flag, end=" ")
    print()
    current_flag_file.close()
  else:
    print("Invalid use of flags.")
elif(len(sys.argv) == 3):
  if(sys.argv[1] == "-update"):
    current_flag_file = open(tag_path,'a')
    current_flag_file.write(" "+sys.argv[2])
    current_flag_file.close()
  elif(sys.argv[1] == "-remove"):
    current_flag_file = open(tag_path)
    current_flags = (current_flag_file.readline()).split()
    current_flag_file.close()

    new_string = ""
    for flag in current_flags:
      if(flag != sys.argv[2]):
        new_string+= (flag + " ") 
 
	#now we overwrite the old tags with new one
    current_flag_file = open(tag_path,'w') 
    current_flag_file.write(new_string)
    current_flag_file.close()
  else:
    print("Invalid use of flags.")    
else:
  print("Invalid use of flags.")




    





import os
import sys

def removefiles(item,tag_list):
  for tag in tag_list:
    if(item.endswith(tag)):
      os.remove(item)
      
#Path to location of the script and the tags
script_loc = os.getcwd()  
tag_path = script_loc+".127pythonscript/.target_tags"  


if(len(sys.argv) == 1):     #Running the default script
  print("Cleaning...")

  home_path = os.getenv("HOME")
  os.chdir(home_path)				

  target_file = open(tag_path)
  target_tags = (target_file.readline()).split()
  target_file.close()

  #Delete target files in home directory
  for item in os.listdir(home_path):
    if os.path.isfile(item) and (not item.startswith(".")): #don't delete hidden files
      removefiles(item, target_tags)

  #Delete target files 1 level down from home. (Ignoring hidden files/directories)
  for content in os.listdir(home_path): 
    if os.path.isdir(content) and (not content.startswith(".")):
      os.chdir(os.path.abspath(content))	#Go down 1 level
      for item in os.listdir(os.getcwd()):
        if os.path.isfile(item) and (not item.startswith(".")):
          removefiles(item, target_tags)
      os.chdir("..") #Go back up 1 level(home)

  os.chdir("Desktop") #Delete everything in desktop
  if len(os.listdir(os.getcwd())) > 0: #Ugly way of checking if empty
    os.system("rm -r *")
  os.chdir(home_path)

  os.chdir("Downloads") #Delete everything in downloads
  if len(os.listdir(os.getcwd())) > 0:  
    os.system("rm -r *")
  os.chdir(home_path)

  os.chdir("Documents") #Delete everything in documents
  if len(os.listdir(os.getcwd())) > 0:  
    os.system("rm -r *")
  os.chdir(home_path)

  print("Done.")  #Done deleting the files.
    
elif(len(sys.argv) == 2):
  if(sys.argv[1] == "-show"):           ### SHOW ###
    current_flag_file = open(tag_path)
    current_flags = (current_flag_file.readline()).split()
    print("Current Targets:")
    for flag in current_flags:
      print(flag, end=" ")
    print()
    current_flag_file.close()
  
  elif(sys.argv[1] == "-uninstall"):    ### UNINSTALL ###
    home_path = os.getenv("HOME")
    os.chdir(home_path)		  #Delete the folder

    alias_file = open(".bash_aliases")          #Delete alias entry

    comment = "#Alias for running a python deletion script for csci127 at Hunter College.\n"
    alias = "cd; cd .127pythonscript; python3 removepy.py; cd;"
    file_line = [comment, alias ]
    new_data =""
    for line in alias_file:
      if (line not in file_line):
        new_data+= line
    alias_file.close()
    alias_file.open(".bash_aliases",'w')
    alias_file.write(new_data)
    alias_file.close()

    print("Script has been removed.")

    os.system("rm -r .127pythonscript")

  else:
    print("Invalid use of flags.")

#Code base for updating the tags.    
elif(len(sys.argv) == 3):

  if(sys.argv[1] == "-update"):        ### UPDATE ###
    current_flag_file = open(tag_path,'a')
    current_flag_file.write(" "+sys.argv[2])
    current_flag_file.close()

  elif(sys.argv[1] == "-remove"):       ### REMOVE ###
    current_flag_file = open(tag_path)
    current_flags = (current_flag_file.readline()).split()
    current_flag_file.close()

    new_string = ""   #Reconstructing the data (excluding the marked tag)
    for flag in current_flags:
      if(flag != sys.argv[2]):
        new_string+= (flag + " ") 
 
    current_flag_file = open(tag_path,'w') #Overwrite the file with new data
    current_flag_file.write(new_string)
    current_flag_file.close()
  else:
    print("Invalid use of flags.")    
else:
  print("Invalid use of flags.")




    





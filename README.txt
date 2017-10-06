The following scripts are written by Jack Chen of Hunter College.

NOTES: 
This script is written with the intention to be run on the laptops
located at 1001E at North Building. Caution when running on other machines.
Python3 should also be installed.
This should obviously be run on a UNIX type system.

To install the script, navigate to the location of this folder. Then
enter "python3 installscripy.py". 

FLAG OPTIONS
-updatetags [new tags]
-showtags [lists all files to be deleted]
-removetag [tag to remove]


MAIN FUNCTIONALITY

The main functionality of these scripts is to remove all files who's tag is 
targeted for deletion. The script will delete all non-hidden files with 
a targeted tag in the home directory and all files that are one level down from
the home directory.
Afterwords, the script will delete EVERYTHING(including directories) within
the Desktop, Downloads and Documents folders.

INSTALLATION NOTES

The folder also comes with an install script, which will copy the script (even
from a USB), into a hidden folder called ".127pythonscript" located at the
home directory. 
Afterwards, it will add an alias command into the hidden .bashrc file located
at the home directory. After closing the terminal, you should be able to 
call the main script by typing "removepy" into the terminal.
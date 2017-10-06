import sys
import os

tag_file = open(".target_tags")
tag_data = (tag_file.readline()).split()
for i in tag_data:
    print(i)
import os
import shutil

path = 'C:/Users/P2938214/Documents/Pytests'

print("Goodbye, World!")
print(os.listdir(path))

source = 'C:/Users/P2938214/Documents/Pytests/FolderA'
destination = 'C:/Users/P2938214/Documents/Pytests/FolderB'

dest = shutil.move(source, destination)

print("These are the results:\n")
print(os.listdir(path))

print("Where the files went:", dest)


sec = input("hi")
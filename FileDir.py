from pathlib import Path

path = Path() #return current directory, can pass a string for abosulte or relative path
print(path)

path = Path("test")
print(path.mkdir())

for file in path.glob('*'): #search all files in a directory
  print (file)


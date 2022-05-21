import math
#import lpmodules
#from lpmodules import module_greeting

#using import and function
print(math.floor(2.2))

#functions
def sayHello(name):
  print(f"Hello {name}!")
  print("Welcome to the team")
  return "Success"

status = sayHello("John")#can call a function only after its definition, positional argument where position of argument is important
print(status)#python return 'None' be default
sayHello(name="John")#keyword argument, where parameter is mapped to argument and hence position does not matter. Can only be used after positional arguments

#excpetion handling
try:
  age = int(input("Enter age: "))
  print(f'Age is {age}')
except ValueError:
  print('Incorrect age format')

#lpmodules.module_greeting()#if importing like import lpmodules
#module_greeting()#if importing like from lpmodules import module_greeting

print("if you create a directory and want it a python package you have to have __inti__.py file in it")

print("to import from a directory you have to do it like import folder.file and then call function on it")
print ("using from folder.file import function1,function2 is always easier way.")
print(" to avoid importing all functions do, from folder import file and you will have all functions access")

#first program, case sensitive
print("Welcome to Learn Python with Arun")
print('*' * 10)#print * 10 times
multiline_comments = '''
This is
multiline comment
'''
print(multiline_comments)

#using variables, can cocatenate only strings
age = 35
print (type(age))#to find type of a variable
print("Age is " + str(age))

#receive inputs from user
#name=input("Enter the name of the user")
print("User name is " + name)
msg = f'{name} is a coder'#formating string with variables
print(msg)

#Type conversion between number, string and boolean int(), float(), str(), bool()
#birth_year = input("Enter user birth year: ")
age = 2022-int(birth_year)
print("User age is ", age)

#strings - immutable same as java
course = 'Python for Beginners'
print('Python' in course)
print(course[-2])#second char from the end
print(course[0:3])#starting char and till but not including last
print(course[5:])
print(course[:5])

#arthimetic operators : +,-,*,/(return float), // (result int), % (modules/remainder), ** (exponential, to the power), +=, -=, *=

#comparison operators : >,<, >=,<=,==,!=

#logical operators : and, or, not
price = 35
print(price>10 and price<30)
print(price>10 or price<10)
print(not price >10)

#if statement
if(price>20):
  print("Price is high")
elif(price>30):
  print("Price is very high")
else:
  print("Price is low")

#while loop
i=1
while (i<10):
  print(i)
  i+=1
  break

#lists
names = ["Test1","Test2","Test3",]
print(names)
print(names[0])
print(names[-2])#second elemnt from last in list
print(names[0:2])#returns new list object
names.insert(2,"Test12")#insert element in list at specific position
print(names)
print("Test2" in names)

#for loop
for name in names:
  print(name)

#range function to generate sequence of numbers
numbers = range(5,15,2)
for num in numbers:
  print(num)

#Tuples - cant be changed once created
numbersTuple = (1,2,3,4,5)#defined in different paranthesis
a,b,c,d,e = numbersTuple #easy assignment to variables

#Dictionaries - key value, unique keys
customer = {
    "name":"john"
    "age":30
}
print(customer["age"])#case sensitive keys
print(customer.get("Age"))#not case sensitive
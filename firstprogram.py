print("Hello World")
print (12+5)
a = 5
b = 23
print(a+b)
print (a, b, 'are a and b respectively')

# Comments in python 


# This is single line comment

""" This 
is
 multi line comment """

""" Python program to demonstrate
 multiline comments"""

# print("Multiline comments")


# Variables in python

age = 21  #integer
_colour = "lilac"   #string
total_score = 90+43    #integer

grand_total = age + total_score

print ("age is ", age)
print (_colour)
print(total_score)
print(grand_total)

# Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.
# example 
x = 10
x = "Now a string"
print(x)


# multiple assignment
a = b = c = 100
print(a, b, c)

# Assigning Different Values
x, y, z = 1, 2.5, "Python"
print(x, y, z)


# Casting a Variable

# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)  
print(cnt)  
print(s2)



li = [1, 2, 3]
d = {'key': 'value'}
bool = True


# Get and print the type of each variable
print(type(a))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))
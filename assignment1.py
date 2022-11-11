# Create 3 variables and assign them a value.
# Create a variable called my_string and assign it a string value
my_string = "my string"
# Create a variable called my_integer and assign it an integer value
my_integer = 5
# Create a variable called my_float and assign it a float value
my_float = 55.5
# # Create two new integer variables with any values.
int1 = 5
int2 = 4
# Write code to add those variables, storing the result in a third variable.
int3 = int1 + int2
# In a comment, write what you expect the value of the third variable to be.
# 9
# Print out the value of the third variable to verify that it has the correct value.
print(int3)
# Create two new float variables with any values.
flt1 = 55.5
flt2 = 54.5
# Write code to add those variables, storing the result in a third variable.
flt3 = flt2 + flt1
# In a comment, write what you expect the value of the third variable to be.
#100
# Print out the value of the third variable to verify that it has the correct value.
print(flt3)
# Create two new string variables with any values.
str1 = "my"
str2 = "string"
# Write code to add those variables, storing the result in a third variable.
str3 = str1 + str2
# In a comment, write what you expect the value of the third variable to be.
#mystring
# Print out the value of the third variable to verify that it has the correct value.
print(str3)
# Add any integer variable and any float variable from the previous steps, storing the result in a third variable.
int_flt1 = flt1+int1
# In a comment, write what you expect the value of the third variable to be.
#60.5
# Print out the value of the third variable to verify that it has the correct value.
print(int_flt1)
# In a comment, write what you expect the type of the third variable to be.
#float
# Add any integer variable and any string variable from the previous steps, storing the result in a third variable.
#str_int1 = int1 + str1
# In a comment, write what you expect the value of the third variable to be.
#i expect an error
# Print out the value of the third variable to verify that it has the correct value.
##print(str_int1)
# In a comment, write what the output value was and an explanation of why that is.
#an error because the interpreter cannot add a str and an int
# Comment out the line of code and go on to the next section.
# For next steps you are going to use Python functions beyond print.
#
# Functions can accept input and may return a result. For example, print takes a message to display on the screen, but other than doing that, doesn’t return any results that we need for now.
#
# Other useful functions are str, which converts a number to a str, round, which takes a number and count of decimals places, and returns the number rounded (so round(6.4352, 3) returns 6.46. Also type takes any variable name and returns its type.
#
# Try these tasks now (in the same python file you're working in):
# Print out the types of my_string, my_integer, and my_float.
print(my_float)
print(my_integer)
print(my_string)
# Create a string variable and assign it an integer value (value should be in quotes).
int_string = "5"
# Print out the type of the new variable to verify it is a string
print(int_string)
# Cast that variable to an integer and store it in a new variable
cast_string = int(int_string)
# Print out the type of the new variable to verify that it is now an integer
print(cast_string)
# Multiply 5 by 7.654321 and round to 3 decimal places. Print out the resulting value.
round(5*7.654321, 2)
# Use the input function to display a message that says “Enter your name” and places the result in a variable called my_name.
name = input("Enter your name")
# Print out the resulting value.
print(name)
# Use the input function to display a message that says “Enter your favorite number” and places the result in a variable called favorite_number.
favorite_number = input("Enter your favorite number")
# Print out the resulting value
print(favorite_number)
# In a comment, write what you expect the type of favorite_number is.
#I expect the type to be string
# Print out the type of favorite_number
print(type(favorite_number))
# In a comment, write down the output and an explanation of why that is. Hint, you may need to search up "python documentation input"
# 5 is being entered as a string type and interpreted as such regardless of what character is entered.
# Now, ask the user for two integers (use the input function twice).
num1 = int(input("please enter a number: "))
num2 = int(input("please enter another number: "))
# Store the sum of the two numbers in a third variable
num3 = num1 + num2
# In a comment, write what you expect the value of the third variable to be.
#3
# Print out the value of the third variable.
print(num3)
# In a comment, write what the output value was and an explanation of why that is.
#i converted the input numbers to int so i expect the interpreter to add 1+2=3

# Day 8 - Functions with Inputs / Arguments & Parameters

# Build a Cipher Program (Caesar Cipher)

# Type 'encode' to encrypt, type 'decode' to decrypt:
# Type your message:
# Type the shift number:
# Here's the encoded result:
# Type 'yes' if you want to go again. Otherwise, type 'no'.

### Functions
### Example: 
######## def my_function():
########    Do this
########    Then do this
########    Finally do this

# Inputs can be passed to functions, inside the parenthesis: 
# def my_function(something)
########    Do this with something
########    Then do this

# my_function(123)

## something -> parameter
## 123 -> argument

# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


## Simple function
def greet():
    print("Hello")
    print("How are you?")
    print("How's family?")


greet()


## Function with input
def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How are you, {name}?")


greet_with_name("Laura")

## Function with multiple inputs
def greet_with(name, location):
  print(f"Hello, {name}")
  print(f"What is it like in {location}?")

greet_with("Laura", "Brazil")

#### KEYWORD ARGUMENTS
# def my_function(a, b, c)
########    Do this with a
########    Then do this with b
########    Finally do this with c

# my_function(c=3, a=1, b=2)

## Function with keyword arguments
def greet_with(name, location):
  print(f"Hello, {name}")
  print(f"What is it like in {location}?")

greet_with(location="Brazil", name="Laura")


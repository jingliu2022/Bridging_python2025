# Quick Start with Python
## Note1: Comments after pound sign won't be executed
## Note2: To run one line of code, place your mouse there,  right-click and choose "Execute Line in Python Console"
## Note2: To run multiple lines of codes, select multiple lines,  right-click and choose "Execute Selection in Python Console"



# 1. Python Basics: Numbers, Strings, List
## 1.1 Numbers and operators
1 + 2            # Addition, try subtraction (-)?
10 * 2           # Multiplication, try division (/)?
30 - 10 * 2      # A more complicated formula

a = 20           # Assignment operators, assign a value (20) to a newly created variable (a)
b = 5
a * b            # Use the two variables

a == 20          # Comparison operators ==, >, <, !=, <=, >=
b != 50

not a < 10               # Logical operator: not, and, or
(a > 10) and (b == 10)   # Two conditions, same as width > 10 and height == 10

## 1.2 Strings
"Hello Everyone"  # Either double quote or single quote are fine
"doesn't"         # Double quote outside, single quote inside (or reverse)

sentence = 'First line.\nSecond line.'    # Create a sentence with multiple lines - break lines with \n
print(sentence)                           # print() will display the contents without quotation mark

# Strings can be indexed, sliced, concatenated.
len(sentence)  # Check the length of a string
sentence[5]    # Select character in the sixth position: python index starts from 0
sentence[-1]   # The last character (use - to index from the end)
sentence[:5]   # Select five three character: index 0,1,2,3,4 only, same as sentence[0:5]
sentence[5:]   # Select all characters starting from the 6th (index 5)

#sentence[0] = 'H'                       # Strings cannot be muted, ERROR here if executed
'1st' + sentence[5:]                     # Replace first 5 characters via concatenating two strings.
'The 2nd ' + sentence[-5:-1] + ' only.'  # More complicated concatenation

## 1.3 Lists
lst1 = [1, 2, 3, 4, 5]      # Create a list variable lst1
1 in lst1                   # Membership operators: in, not in
lst1[0]                     # Lists can be indexed as well
lst1[3:]                    # Select all elements starting from the 4th
lst1[0] = 'one'             # Unlike strings, lists are mutable.


# 2. Flow Control
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    # Create another list variable lst2

## 2.1 The for-loop (Execute Selection)
for i in lst2:
    print(i * 10 + 1)     # Indented (press the tab key)

## 2.2 The if-else statement
if 2 in lst2:
    print("We find it!")
else:
    print("Unfortunately, we cannot find it!")

## 2.3 Combine for-loop and if-else statement
for i in lst2:
    if i <= 4:  # 1st indentation
        print(i, "is in the bottom.")  # 2nd indentation
    elif (i > 4) and (i <= 7):
        print(i, 'is in the middle.')
    else:
        print(i, "is in the top.")


# 3. Python functions and Modular Programming
## 3.1 Built-in functions
round(13.136784, 2)    # round a number to certain decimal places
pow(4, 3)              # same as 4**3

## 3.2 Define a custom function
## Define two functions
def greet(name):
    print("Hello, " + name + ". How are you today?")

def compare(a, b):
    if a < b:
        print(str(a) + " is smaller than " + str(b) + ".")
    elif a > b:
        print(str(a) + " is greater than " + str(b) + ".")
    else:
        print(str(a) + " is equal to " + str(b) + ".")

## Apply the two functions by feeding param values
greet('Alice')
compare(2.0, 2)


##  3.3 Modular Programming
## Step 1: save the above codes in 3.2 in a new python file and name the file as my_module.py
## Step 2: import the module, run those functions by assigning new param values
import my_module
help(my_module)              # Check the information of the module first

my_module.greet('Richard')   # Use functions after the module name with the .method
my_module.compare(1, 2)

from my_module import greet  # We can also import a function from a module directly
greet('Alice')


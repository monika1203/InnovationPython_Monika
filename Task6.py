# 1. Write a program to Python find the values which is not divisible 3 but is
# should be a multiple of 7. Make sure to use only higher order function.

def myfun(X):
    if (X % 3 != 0) and (X % 7 == 0):
        return X


list(filter(myfun, range(20)))


# 2. Write a program in Python to multiple the element of list by itself using
# traditional function and pass the function to map to complete the operation.

def func(x):
    return x ** x


list(map(func, [1, 2, 3, 4, 5]))

# 3. Write a program to Python find out the character in a string which is
# uppercase using list comprehension.

word = "Python Training ConsutADD"
[i for i in word if i.isupper()]

# 4. Write a program to construct a dictionary from the two lists containing the
# names of students and their corresponding subjects. The dictionary should maps
# the students with their respective subjects. Let’s see how to do this using for loops
# and dictionary comprehension. HINT-Use Zip function also
# ● Student = ['Smit', 'Jaya', 'Rayyan']
# ● capital = ['CSE', 'Networking', 'Operating System']

# 1st way
dict(zip(['Smit', 'Jaya', 'Rayyan'], ['CSE', 'Networking', 'Operating System']))

# 2nd way
Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

mydict = {}

for k in Student:
    for v in capital:
        mydict[k] = v
print(mydict)


# 5. Learn More about Yield, next and Generators

# 6. Write a program in Python using generators to reverse the string. Input String
# = “Consultadd Training”

def rev(x):
    length = len(x)
    for i in range(length - 1, -1, -1):
        yield x[i]


mystring = "ConsultADD Training"
for char in rev(mystring):
    print(char)


# 7. Write any example on decorators.

def add(number):
    return number + 1


def multiply(function):
    number_to_multiply = 5
    return function(number_to_multiply)


multiply(add)

# 8. Learn about What is FRONT END and its Technologies and Tools
# ● Make sure to mention at least 5 top notch technologies of Frontend.
# ● Also mentioned the name of companies using those 5 technologies individually


# Following are the Top notch Frontend technology:
''' AngularJS  --- Google, Udemy, and Amazon.
JavaScript --- PayPal, Microsoft , Netflix
HTML ---reddit, StackShare, and Lyft
React --- Uber, Airbnb, and Facebook.
Bootstrap --- Spotify, Udemy , Twitter '''


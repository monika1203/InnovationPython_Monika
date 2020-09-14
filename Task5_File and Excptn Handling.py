# 1.  Write a program in Python to allow the error of syntax to go in exception.

try:
    eval("X === X")
except SyntaxError:
    print("Syntax is wrong, Please provide the correct syntax")

# NOTE: SyntaxErrors get raised when the file/code is parsed, not when that line of code is executed. The reason for
# this is simple. If the syntax is wrong at a single point in the code, the parser can't continue so all code after
# that line is un-parseable. In other words, We can only catch syntax errors when python is trying to parse
# something. This includes exec, eval,input(), import

# 2.Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect
# throw an exception and ask them to enter the name again. Make sure to use read only mode.

from sys import argv

programname, filename = argv
print("The name of program is:", programname)
print("The name of  code file is:", filename)

while True:
    try:
        with open(filename, 'r') as file1:
            content = file1.read()
            print(content)
            break
    except:
        print("Given File name is wrong! Please provide correct name")

        try_again = input("Do you want to try again!! Press Yes and No:")
        if try_again == "Yes":
            filename = input("Enter the correct file name:")
        elif try_again == "No":
            break

# 3. Write a program to handle an error if the user entered the number more than four digits it should return “Please
# length is too short/long !!! Please provide only four digits”

while True:
    try:
        X = int(input("Enter a number: "))
        if len(str(X)) == 4:
            print(X)
            break
        else:
            raise Exception
    except:
        print("Please length is too short/long !!! Please provide only four digits\n")

# 4. Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password
# and if the password is incorrect give chance to enter it again but it should not be more than 3 times.

useremail = input("Enter the user email id:")
pwd = input("Enter the password:")
count = 0
while True:

    try:
        re_type_pwd = input("Re-type the password:")
        if re_type_pwd == pwd:
            print("successfully created login page ")
            break
        else:
            raise Exception
    except:
        if count < 3:
            print("Please Enter the password again:")
            count = count + 1
        else:
            print("Entered incorrect password 3 times")
            break

# 5.  https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and
# Raise concept.

#DONE


# 6. Read any file using Python File handling concept and return only the even length string from the doc.txt
# file.Consider the content as:

'''Consider the content as: 
	Hello I am a file 
	Where you need to return the data string 
	Which is of even length 
	Make sure you return the content in 
	The same link as it is present.'''

with open('Document.txt', 'r') as xfile:
    for line in xfile:
        line = line.rstrip()
        if len(line) % 2 == 0:
            print(line)
        else:
            continue


#7. Replace vowels with letter X

words = "ConsultADD"
vowels = 'aeiou'
mylist = []
for word in words:
    if word.lower() in vowels:
        #print(word)
        word = word.replace(word, 'X')
    mylist.append(word)

print(''.join(mylist))

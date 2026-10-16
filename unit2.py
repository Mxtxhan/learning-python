print(20)
#This is an integer, it's an integer number.
a = 41
print(type(a))
#The class shown as "int" stands for integer.
print(1.4)
#This is a float, it's a decimal number.
b = 6.71345
print(type(b))
#The class shown is "float".
print(True)
print(False)
#These are Boolean classes, they only are True/False.
c = True
print(type(c))
#The class shown as "bool" stands for boolean.
print("Hi")
#This is a string, it's just words... i mean...
d = "Welcome to Python"
print(type(d))
#The class shown as str stands for string.


# The a, b, c, d are called VARIABLES. Creating a variable has to follow some rules:
# 1) Variable names cannot start with numbers, but it can end with or contain numbers.
k1h2 = "a 'string' variable"
#12kh will show an error!

# 2) A variable name can be defined more than one, however only the last definition will be valid...
number1 = 10
print(number1)
number1 = 20
print(number1)
# ...unless if added a mathematical operator before = will assign the output of the equasion to the same variable.
print(number1)
number1 += 30
print(number1)

# 3) Variable definitions are case sensitive!
example = "im an example"
Example = "im the other example with a capital e so i'm way cooler"
print(example)
print(Example)

# 4) Space cannot be used.


#NOTE: Definitions can be made in only one line as well.
x, y, z = (1, "y", True)



# MATHEMATICAl OPERATORS
'''
Sum = +
Minus = -
Multiply = *
Division = /
Power = **
Whole Division = //
Mod = %

'''

print (a + b)
print(number1 ** b)
print(a / number1)

#String summation merges the characters assigned.

print(example + ", " + "Hi" + " "+ d)
print(":]")



#EXAMPLE:
'''
Create a set of variables for a customer and welcome it to the system:
Customer Name
Customer Surname
Customer Name Surname
Customer Gender
Customer SSN
Customer Birth Year
Customer Adress
Customer Age
'''
nameCustomer = "Metehan"
surnameCustomer = "Bayhan"
namesurnameCustomer = nameCustomer + " " + surnameCustomer
genderCustomer = "M"
ssnCustomer = "11111111111"
byCustomer  = 2007
adrCustomer = "Python Road, No: 11/11, Cankaya/Ankara/TURKIYE"
ageCustomer = 2026 - byCustomer

print("Welcome " + nameCustomer + ".")



# Input and Variable Conversion

# input command lets the user enter the value of a variable IN STRING
# so in some occasions, we must reclass the string (ex. string --> int)

enter1 = input("Enter the first number of the summation ")
enter2 = input("Enter the second number of the summation ")
summation = enter1 + enter2
print(summation)
# print will show 1221 as the string summation, enter1 and enter2 should be transformed
# into int.
print(type(enter1))
print(type(enter2))
enter1 = int(enter1)
print(type(enter1))
# TRANSFORMED INTO INT!
enter2 = int(enter2)
print(enter1 + enter2)
# all the conversions can be used with "int, bool, str, float" etc. ( true to int = 1, f = 0)
# NOTE: when printing or doing summation with str, other classes will not sum.
# so str(int value) should be used after mathematical calculations.
# \n gets the string into one line down
# NOTE: Every string starts with char 0 and ends with char n. All the chars can bee
# seen with command len, len-1 will show all the char numbers, EX:
# Hello World.
# 0 1 2 3 4 5 6 7 8 9 10 11 (left to right char system)
# =======================
# -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 (right to left char system)
# len= 12
len2 = "learning python"
print(len(len2))
print(len2)
# adding [char number] to the end of the str will only print that char
print(len2[2])
# adding [first char number : end char number] to the end of str will print that chars 
# & between (END NOT ADDED)
print(len2[1:6])
# not adding first char number will start from the beggining and end in end char number
#(END NOT ADDED)
# alike, not adding end char number will start at first char number and end at the end of str
#(END NOT ADDED).
# adding [first char number : end char number : mod] to the end of str
# will print that chars & between skipping mod (END NOT ADDED)
len3 = "0123456789"
print(len3[0:8:2])



# STRING FORMATTING
"""
Arguments can be added in strings with the help of {}, and afrer .format()
.format will take the arguments in the order; 0,1,2,3...
We can numerise the arguments ourselves to change the order of .format
{1} {0} {3} {2}
or can name the arguments then order the format ourselves
{n} {u} .format (n=variable1, u=variable2)
 NOTE: formatting does NOT require conversation when printing strings, int's can stay etc.
 NOTE: when formatting floats. {float: x.y} parameters can be used, this parameters
 determine x: spaces for the whole part, y:characters in decimal

 NOTE: .format can be directly shortened like f"string {var directly here}"

"""
 # REFER TO string_ex.py for applicational question solutions.



 #STRING METHODS
"""
Just like .format, there are many other string methods.
.upper = UPPERCASE STRING
.lower = LOWERCASE STRING
.title = ALL THE INITIALS UPPERCASE
.capitaliZe = STR'S FIRST INITIAL WILL BE UPPERCASE
.strip = DELETES THE SPACE AT FIRST AND LAST CHARS IF WHITESPACE (space, tabs, trails, etc.)
.split = GIVES A LIST DECIDED BY SPACES
"joinedbywhat".join(str) = MERGES THE LIST DIVIDED BY .split
.find = FINDS THE GIVEN PRMTR IN STR (-1: not there, any other: starts with that char)
.startswith = GIVES A BOOL ON STR'S INITIAL'S STATUS ON PRMTR
.endswith = GIVES A BOOL ON STR'S ENDING'S STATUS ON PRMTR
.replace("","") = REPLACES ALL PRMTR FOUND IN STR WITH SECOND PRMTR
.center("","") = CENTERS THE STR IN GIVEN PRMTR SIZED BOX, BOX FILLED WITH SECOND PRMTR

parameters can be defined (ex .split(.) will give a set decided by dots.)
NOTE: That these are methods, () should be done even if no parameters specified.
NOTE: a string can have multiple methods, ex: str.strip().split(.) etc.
NOTE: These are the most used. Every method can be found on:
https://www.w3schools.com/Python/python_ref_string.asp
 examples can be found on string_methods_ex.py
""" 
# You can create string lists by defining a variable with []
first_list = ["bir", 2, True, 5.6]
print(first_list)
#Lists can be treated like a string variable. (summation, len, etc.)
# Multiple lists can be added into a main list and be treated like
# seperate vars.
sec_list = ["iki", 1, False, 6.5]
mlist = [first_list, sec_list]
print(mlist)
#Refer to lists_ex.py for demo on lists.
#min(notamixedlist) #selects the smallest number / first in alphabet in given list
#max(notamixedlist) #selects the largest number / last in alphabet in given list
#There are methods in lists just like in strings.
mlist.append("addasomethinghere") #adds the bracketed value to the end of the list
mlist.insert(2,"addthisbeforeaddsomethinghere") #adds the 2nd parameter before the number char first parameter
sec_list.pop() #removes the parametered character
sec_list.remove(1) #removes the parametered VALUE!
#notamixedlist.sort() #sorts the list by alphabeticly / numericly
sec_list.reverse() #reverses the list by the given order
first_list.count(2) #counts how many parametered values there are in the given list
first_list.clear()
sec_list.clear()               #clears the list and makes the set empty ( [] )
mlist.clear()
# Tuple's exists as well, they are just like lists but cant be assigned/changed afterwards of definition.
# Tuple definition is made with tuplenamevar = "x0" ,"y"   or for better reading tuplenamevar = ("x0", 2)
hituple = (4, "hi")
# There's another list like class, caled dictionary, check this:
sehirler = ["sakarya" , "ankara" , "kayseri"]
plakalar = [54 , 6 , 38]
print("Ankara'nın plakası şudur: " + str(plakalar[sehirler.index("ankara")]))
# Thats not lightweight at all, and the indexes should be equal. For calling another info with an info, we create DICTIONARIES.
# They are defined by {} instead of [] like lists. The first var is KEY, then the called var will be VALUE
plakadict = {"ankara":6, "sakarya":54, "kayseri":38}
print(plakadict["ankara"])
# Dict's can be assigned/changed unlike tuple's
# Dict key's can be added into new keys!
user = {"Metehan": {
"age":20,
"gender":"M",
"address":"Ankara",



}
        
        
        }

print(user["Metehan"])
print(user["Metehan"]["address"])

#There's another data type, called SETS. Sets cannot be indexed, and defined with {} like dicts however without :value
# Works in for loops, will be covered
fruits = { "banana", "cucumber", "eggplant"}

for hoho in fruits:
    print(hoho)

# can be added new vars with .add()
# can be added new vars SIMULTANIOUSLY with .update(["new1", "new2"])etc. and can only contain one SAME variable!
# sets have .discard() instead of .remove


#IN VALUE TYPES ( int float str bool), ASSIGNABLE DATA IS SEPERATE.
abc= 1
cba = 2
abc = cba
cba = 3
print(abc, cba)
#BUT IN REFERENCE TYPES (list and subtypes of lists), ASSIGNABLE DATA IS CONNECTED!
klm = ["hi", "hello", "whats up"]
yht = ["what", "you", "sayin?"]
klm = yht
yht[0] = "wow"
yht[2] = "azaelia banks?"
print(klm , yht)
'''
END OF UNIT2

'''
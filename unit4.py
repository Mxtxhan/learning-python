# What's if?
'''
If statements are used to execute code based on a condition.
'''
if 3>2:
    print("3 is greater than 2")
if 3<2:
    print("you cant see this on terminal")

#What's else?
'''
The else statement is used to execute code when the if condition is not met.
'''


print("Welcome, please log in.")
usrname = input("Enter your username: ")
usrpass = input("Enter your password: ")

isLoggedin = usrname == "admin" and usrpass == "123"
if isLoggedin:
    print("Welcome back")
else:
    print("Credential(s) are wrong.")


#What's elif?
'''
The elif statement is used to check multiple conditions.
'''
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
if x > y:                        # bu durumda böyle yap
    print("x is greater than y")
elif x == y:                    #şu durumda böyle yap
    print("x is equal to y")
else:                        #diğer durumlarda da bunu yap
    print("x is greater than y")

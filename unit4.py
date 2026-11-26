            #           UNIT 3: OPERATORS IN PYTHON         #

x, y, z = 5, 10, 20
print(x, y, z)
x, y = y, x
print(x, y, z)
x += 5   #x = x+5
x -= 5   #x = x-5
x *= 5   #x = x*5
x /= 5   #x = x/5
x %= 5   #x = x%5
x //= 5  #x = x//5
x **= 5  #x = x**5

#Comparision Operators
password = 123
user = "mxtxhan"
a, b, c,d = 5, 5, 10, 4
result = (a == b) #true
result = (a == c) #false
result = (input("Enter your username: ") == user) #true or false
print(result)
result = (input("Enter your password: ") == password) #true or false
print(result)
# != >>> NOT EQUAL TO
result = (a != b) #false
result = (a != c) #true
result = (a > c) #false
result = (a < c) #true
result = (a >= b) #true

#Logical Operators
x=6
result = 5 < x < 10
print(result) #true

'''
We can use logical operators to combine conditional statements:
AND: Returns True if both statements are true
OR: Returns True if one of the statements is true
NOT: Reverse the result, returns False if the result is true
'''
result = x > 5 and x < 10 #true 
print(result)
result = x > 5 or x < 10 #true
print(result)
result = not(x > 5 and x < 10) #false
print(result)

#n, 5-10 arasında olan bir çift sayı mı?
n= int(input("sayı giriniz: "))
print(n > 5 and n < 10 and n % 2 == 0) 


#Identiy Operators, is is not
x = y = [1,2,3]
z= [1,2,3]
print(x == y) #true
print (x == z) #true
print(x is y) #true
print(x is z) #false
# Whats the difference between == and is?
# == compares the values of both the operands and checks for value equality.
# is checks whether both the operands refer to the same object in memory or not.
# "ADRESS" of the object in memory is checked by is operator.
print(x is not z) #true
print(x is not y) #false


#Membership Operators, in, not in
x = ["apple", "banana"]
print("banana" in x) #true
print("banana" not in x) #false
name = input("Enter your name: ")
print("a" in name) #true or false
print("i" not in name) #true or false
# Loops: For

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# What happened here?
# The for loop iterates over each element in the numbers list and assigns it to the variable num.
# Then, it prints the value of num.
# Num is a variable name, it can be anything, but it is a good practice to use meaningful names.


names = ["Çınar", "Mert", "Ahmet", "Ayşe"]
for name in names:
    print(f"my name is {name}")

name = "Metehan"

for harf in name:
    print(harf)

# Why did this happen?
# The for loop iterates over each character in the string name and assigns it to the variable


tuple = ("apple", "banana", "cherry")
for t in tuple:
    print(t)


binary = [(1,2), (3,4), (5,6)]
for a, b in binary:
    print(a)

#what happened here?
# The for loop iterates over each tuple in the binary list and 
# unpacks the values into the variables a and b. Then, it prints the value of a.


dict = {"k1": 1, "k2": 2, "k3": 3}

for item in dict:
    print(item)

#just keys are printed, if you want to print values, you can use dict.values() method.

for item in dict.items():
    print(item)

#dict.items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
# and dict.values() method returns a view object that displays a list of all the values in the dictionary.

for values in dict.values():
    print(values)


'''
So, nothing = just keys
dict.items() = key-value pairs
dict.values() = just values
'''

# Loops: While
x = 0
while x <= 100:
    print(x)
    x += 1

print("bitti")

x = 0
while x <=100:
    if x % 2 == 0:
        print(x)
    x += 1

# What happened here?
# The while loop continues to execute as long as the condition x <= 100 is true.
# Inside the second loop, it checks if x is even (x % 2 == 0) and prints it if so.
# Then, it increments x by 1.

# "" = False
name = ""
while not name.strip():
    name = input("Enter your name: ")

print(f"Hello, {name}!")

# Break and Continue
# Break statement is used to exit the loop when a certain condition is met.
# Continue statement is used to skip the current iteration and continue with the next iteration.
for letter in "Python":
    if letter == "h":
        break
    print(letter)
    # The loop will break when it encounters the letter "h", so it will only print "Pyt".

for letter in "Python":
    if letter == "h":
        continue
    print(letter)
    # The loop will skip the letter "h" and continue with the next iteration, so it will print "Pyt on".

    '''
    Continue = atla
    Break = bitir
    '''

x = 0
while x < 5:
    if x ==2:
        break
    print(x)
    x += 1


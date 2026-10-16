# User Defination Process
print("         *** WELCOME TO ***" + "\n   TYT Net Calculator & Study Card ")

print(">> Please Log In.")
name = " ".join(input("NAME: ").split()).title()
surname = " ".join(input("SURNAME: ").split()).title()
print("         *** WELCOME " + name + " " + surname + " ***")


# Defination and Gathering of TYT Correct and False Questions
print(name + ", Please Log Your TYT Questions")
print(">>TURKISH:")
turkish = (input("Your Correct Questions: "), input("Your False Questions: "))

print(">>SOCIAL STUDIES:")
social = (input("Your Correct Questions: "), input("Your False Questions: "))

print(">>MATHEMATICS:")
mathgeo = (input("Your Correct Questions: "), input("Your False Questions: "))

print(">>SCIENCE:")
science = (input("Your Correct Questions: "), input("Your False Questions: "))


# Calculation of Nets.
netturkish = int(turkish[0]) - (int(turkish[1])/4)
netsocial = int(social[0]) - (int(social[1])/4)
netmathgeo = int(mathgeo[0]) - (int(mathgeo[1])/4)
netscience = int(science[0]) - (int(science[1])/4)


# Printing Output To User
print("Calculated!")
print("TYT RESULT CARD".center(50 , "*"))
print("Student: " + name + " " + surname)
print(">>NETS:")
print(f"{'>TURKISH: ':<16}{'>SOCIAL: '}")
print(f"{netturkish:<16.2f}{netsocial:.2f}")
print(f"{'>MATHEMATICS: ':<16}{'>SCIENCE: '}")
print(f"{netmathgeo:<16.2f}{netscience:.2f}")
print("TYT NET:".center(50 , "-"))
print(str(netturkish + netscience + netsocial + netmathgeo) + " NET(S)")
print("Happy Studying, " + name + "!")
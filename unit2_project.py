# User Defination Process
print("         *** WELCOME TO ***" + "\n   TYT Net Calculator & Study Card ")

print(">> Please Log In.")
name = input("NAME: ")
surname = input("SURNAME: ")
name = name.strip()
surname = surname.strip()
name = name.replace(" ", "")
surname = surname.replace(" ", "")
name = name.lower()
surname = surname.lower()
name = name.capitalize()
surname = surname.capitalize()
print("         *** WELCOME " + name + " " + surname + " ***")


# Defination and Gathering of TYT Correct, False and Blank Questions
print(name + ", Please Log Your TYT Questions")
print(">>TURKISH:")
turkish = [input("Your Correct Questions: "), input("Your False Questions: "), input("Questions You Left Unanswered: ")]
print("SYSTEMCHCK: " + str(turkish))

print(">>SOCIAL STUDIES:")
social = [input("Your Correct Questions: "), input("Your False Questions: "), input("Questions You Left Unanswered: ")]
print("SYSTEMCHCK: " + str(social))

print(">>MATHEMATICS:")
mathgeo = [input("Your Correct Questions: "), input("Your False Questions: "), input("Questions You Left Unanswered: ")]
print("SYSTEMCHCK: " + str(mathgeo))

print(">>SCIENCE:")
science = [input("Your Correct Questions: "), input("Your False Questions: "), input("Questions You Left Unanswered: ")]
print("SYSTEMCHCK: " + str(science))


# Calculation of Nets.
netturkish = int(turkish[0]) - (int(turkish[1])/4)
netsocial = int(social[0]) - (int(social[1])/4)
netmathgeo = int(mathgeo[0]) - (int(mathgeo[1])/4)
netscience = int(science[0]) - (int(science[1])/4)


# Printing Output To User
print("Calculated!")
print("TYT RESULT CARD".center(50 , "*"))
print("Student: " + name.upper() + " " + surname.upper())
print(">>NETS:")
print(">TURKISH:        >SOCIAL")
print(str(netturkish) + "             " + str(netsocial))
print(">MATHEMATICS     >SCIENCE")
print(str(netmathgeo) + "            " + str(netscience))
print("TYT SCORE:".center(50 , "-"))
print(str(netturkish + netscience + netsocial + netmathgeo) + "NET(S)")
print("Happy Studying, " + name + "!")

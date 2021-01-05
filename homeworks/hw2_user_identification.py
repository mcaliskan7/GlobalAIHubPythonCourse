information = list()

name = input("Your name: ")
information.append(name)

last_name = input("Your last name: ")
information.append(last_name)

age = int(input("Your age: "))
information.append(age)

birth_year = int(input("Your date of birth: "))
information.append(birth_year)

for i in information:
  print(i)
  
if age < 18:
  print("You can't go out because it's too dangerous!")
else:
  print("You can go out to the street.")

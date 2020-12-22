n0 = int(input("Enter an integer: ")) #allows only integers as integer type
n1 = float(input("Enter a float: "))  #allows integers and floats as float type
n2 = input("Enter a string: ")        #allows anything as string type 
n3 = float(input("Enter a float: "))  #allows integers and floats as float type
n4 = int(input("Enter an integer: ")) #allows only integers as integer type

print(n0,n1,n2,n3,n4)

print("Type of {}: {}".format(n0,type(n0)))
print("Type of {}: {}".format(n1,type(n1)))
print("Type of {}: {}".format(n2,type(n2)))
print("Type of {}: {}".format(n3,type(n3)))
print("Type of {}: {}".format(n4,type(n4)))

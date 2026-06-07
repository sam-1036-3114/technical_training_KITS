list=[10,30,25,40,15,20]
print(10 in list)
print(50 in list)
print(10 not in list)
print(50 not in list)
# identity operator 
# the identity operator compare the memory locations of two objects
#hence it is ,possible to know  whether two ojects are same or not
# maily 2 'is' and 'is not'
num1=10
print(num1)
print(id(num1))
num2=10
print(num2)
print(id(num2))
print(num1 is num2)
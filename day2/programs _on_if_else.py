#w rite a python program to read the month number and print the days in  the month
month=int(input("Enter the month number: "))
print("the number of days in monnth: ",31 if month in [1,3,5,7,8,10,12] else 30 if month in [4,6,9,11] else 28 if month==2 else "invalid month number")
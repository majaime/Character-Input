import datetime
name = input("Enter your name: ")
age = input("Enter your age: ")
age_to_100 = (100 - int(age)) + datetime.datetime.now().year
print(name + ", " + "in the year " + str(age_to_100) + " you will turn 100 years old!")

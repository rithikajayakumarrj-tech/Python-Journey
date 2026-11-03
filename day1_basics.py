print("Hello python")

#personal information

name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_subject = input("Enter your favourite subject: ")

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My favourite subject is {favorite_subject}.")


#age calculator
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print(f"You are {age} years old.")
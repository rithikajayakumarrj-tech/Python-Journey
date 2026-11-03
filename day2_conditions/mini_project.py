#Grade calculator

name=input("Enter the name:")
dept=input("Enter the department:")
mark1=int(input("Enter the mark1:"))
mark2=int(input("Enter the mark2:"))
mark3=int(input("Enter the mark3:"))
total=mark1+mark2+mark3
average=total/3
print("--------------------------------")
print("         GRADE CALCULATOR       ")
print("--------------------------------")
print(f"Name: {name}")
print(f"Department: {dept}")
print(f"Total marks: {total}")
print(f"Average marks: {average}")
if average>=90:
    print("Grade: A | PASS ")   
elif average>=80:
    print("Grade: B | PASS")
elif average>=70:
    print("Grade: C | PASS")
elif average>=60:
    print("Grade: D | PASS")
else:
    print("Grade: F | FAIL")

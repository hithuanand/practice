#Typecasting - converting one variable to another data type

name = "Hithu Anand"
age = 25
gpa = 9.8
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(age)

#age+=1 #TypeError


age+="1"
print(age)

#name="" check if somebody has entered their name
name = bool(name)
print(name)

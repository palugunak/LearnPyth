# running through the loop

students = ["Hermione","clasuter","phobia"]
for student in students:
    print(student)
print("\n")    

for i in range(len(students)):  
    print(i+1, students[i], sep=",")


# ======================================

names = []
for _ in range(3):
    names.append(input("what is your names"))

for name in sorted(names):
    print(f"hello, {name}")   

# =============================================

# storing names in an file

name = input("what's the name ")

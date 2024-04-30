""" x = float(input("enter the first number") )
y = float(input("enter the second number"))

z = round(x+y)



print(f"{z:,}")

# round x +y2.54.5
print(f"{z:.2f}")


"""

x = int(input("enter x"))
y = int(input("enter y"))

if(x < y):
    print("x is less than y")
elif( x > y):
    print("x is greater than y")
else:
    print("x is equal to y")        


if( x < y or x > y):
    print("x is not equal to y")
else:
    print("x is equal to y")   


score = int(input("score:"))
if( score >= 90 and score <= 100):
    print("Grade A") 

elif( score >= 80 and score <= 90): 
    print("Gradd B")    
else:
    print("Grade f")      





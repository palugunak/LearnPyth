a = int(input("enter a value "))
b = int(input("enter a value of b "))


if a > b:
    print(" a is greater than b")
else:
    print("b is greater5 than a  ")    


maxval = a if a > b else b
print(maxval)

 #enhanced the function 

def main():
    x = get_integ("what is x value")
    print(f"x is {x}")
    

def get_integ(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()


"""

def main():
    x = get_integ()
    print(f"x is {x}")
    

def get_integ():
    while True:
        try:
            return int(input("what s x ?"))
        except ValueError:
            pass

main()

"""
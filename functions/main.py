


def main():
    
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("enter the number of dogs"))
        if n > 0:
            return n        
    

def meow(n):
    for _ in range(n):
        print("bark barks barking")


main()


"""
def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")

    
main()


def main():
    print_row(4)


def print_row(width):
    print("?" * width)



main()

"""




"""
def main():
    print_square(6)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end=" ")
        print()       

main()
"""

def main():
    print_square(9)

def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
     print("#" * width)



main()
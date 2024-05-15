# count the number of words in a line or string3
       
      
def main():
    x = get_string()
    print(f"number of words in a string  {x}")


def get_string():
    while True:
        try:
            x = (input("enter the string "))
            words = x.count(" ") +1
            return words

        except ValueError:
            print("x is not an string")


        
main()
   

# example input {'cards': [13, 11, 10, 7, 4, 3, 1, 0]


cards = [13, 11, 10, 7, 4, 3, 1, 0]

def main():
   locate_cards(cards,query)



query = 7 
def locate_cards(cards, query):
    i =0
    while True:
     if(cards[i] == query):
        return i
     
    i += 1
    if i == len(cards):
       return -1

    
main

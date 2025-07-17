class Player :
    def __init__(self):
        self.name = ""
        self.symbol = ""
    
    def choose_name(self) :
        while True :
            name = input ("entre your name player : ")
            if name.isalpha() :
               self.name = name
               break
            print("Invalid name. plase use letters only .")

    def choose_symbol(self) :
        while True :
            symbol = input (f"player 1 {self.name} entre your symbol : ")
            if symbol.isalpha() and len(symbol) == 1 :
               self.symbol = symbol.upper()
               break
            print("Invalid name. plase use a single letters .")

class Menu :
    def start_main(self) :
        x = """
          welcome to my X-0 game
          1 - Start Game
          2 - Quit Game
          entrer your choose 1 et 2 :
    """
        choose = input(x)
        return choose
    
    def End_main(self) :
        x = """
          Game OVER!!
          1 - restart Game
          2 - Quit Game
          entrer your choose 1 et 2 : """
        choose = input(x)
        return choose
    
class board :

    def __init__(self):
        self.borad = [1,2,3,4,5,6,7,8,9]
    
    def display_board(self) :
        pass

    

n = [1,2,3,4,5,6,7,8,9]
j = 0
for i in n :
    j += 1
    if i == j :
       x = f"""
        {j}|{n}|{n}
       -------------
        {n}|{n}|{n}
       -------------
        {n}|{n}|{n}
       """
print(x)
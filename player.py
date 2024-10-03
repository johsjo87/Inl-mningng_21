from deck import Deck 

class Player:
    # initierar en spelare med namn och poäng
    def __init__(self, name: str = "player") -> None:
        self.name: str = name
        self.score: int = 0  
    # metod som frågar om spelaren vill ha ett kort   
    def ask_to_draw_card(self) -> str:
        while True:
            choice: str = input(f"{self.name} Vill du ha ett kort? (ja/nej) ").lower()
            if choice in ["ja", "nej"]:
                return choice
            else:
                print("Välj JA eller NEJ")
    
    # metod som ger spelaren kort
    def draw_card(self, deck: Deck) -> None:
        card_name, card_value = deck.draw_card()
        if card_name == "ess":
            card_value = self.choose_ace_value() # låter spelaren välja sitt värde för ess
            
        self.score += card_value # uppdaterar spelarens poäng
        print(f"{self.name} drog {card_name} poängen är nu {self.score}")
        
    # Metod för att bestämma om värdet på ess ska vara 1 eller 14  
    def choose_ace_value(self) -> int:
        while True:
            choice: str = (input("Vill du att ess ska vara 1 eller 14? "))
            if choice in ["1", "14"]:
                return int(choice)
            
    # kontrollerar om spelaren gått över 21
    def bust(self) -> bool:
        return self.score >21
    # kontrollerar om spelaren fått 21
    def win(self) -> bool:
        return self.score == 21

            
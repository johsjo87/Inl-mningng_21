from deck import Deck

class Dealer:
    # initierar en dealer med namn och poäng
    def __init__(self, name: str = "Dealer") -> None:
        self.name: str = name
        self.score: int = 0
    
    # metod för att dra kort
    def draw_card(self, deck: Deck) -> None:
        card_name, card_value = deck.draw_card() # slumpar ett kort från leken
        if card_name == "ess":
            # väljer alltid 14 på ess om det inte gör så att dealern går över 21. Annars 1
            card_value = 14 if self.score +14 <=21 else 1 
            
        self.score += card_value # uppdaterar dealerns poäng
        print(f"{self.name} drog {card_name} nu är poängen {self.score}") 
    
    # kontrollerar om dealern går över 21
    def bust(self) -> bool:
        return self.score >21 # returnerar True om poängen överstiger 21
    # kontrollerar om dealern fick 21
    def win(self) -> bool:
        return self.score == 21 # returnerar True om poängen är 21
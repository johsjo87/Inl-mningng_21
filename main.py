from deck import Deck
from player import Player
from dealer import Dealer

def play() -> None:
    player = Player("Player") # skapar en spelare
    dealer = Dealer("Dealer") # skapar en dealer
    deck = Deck() # skapar en kortlek
    
    print(f"{player.name} börjar med att få ett kort ") # skriver ut att spelaren får sitt första kort så spelet kan börja
    player.draw_card(deck) # ger spelaren sitt första kort
    
    while True:
        # Frågar om spelaren vill ha ett kort
        if player.ask_to_draw_card() == "ja":
            player.draw_card(deck) # spelaren drar ett kort
            if player.bust(): # kontrollerar om spelaren går över 21
                print(f"{player.name} du fick över 21. Du förlorade ")
                return # avslutar spelet för spelaren
            elif player.win(): # kontrollerar om spelaren fick 21 och därmed vann
                print(f"{player.name} fick 21. Du Vann!! ")
                return # avslutar spelet
        else:
            print(f"{player.name} stannade med {player.score} poäng ") # meddelar att spelaren stannar
            break # avslutar spelarens tur när den har stannat
        
    # dealern drar kort sålänge dealerns poäng är under spelarens och dealern inte gått över 21    
    while dealer.score < player.score and dealer.score <=21:
        dealer.draw_card(deck) 
        if dealer.bust(): # kontrollerar om dealern gått över 21
            print("Dealern gick över 21. Du vann! ")
            return # avslutar spelet
        elif dealer.win(): # kontrollerar om dealern fick 21 
            print("Dealern fick 21. Du förlorade ")
            return # avslutar spelet
            
    # jämför spelarens och dealerns poäng för att avgöra vinnaren
    if dealer.score > player.score and dealer.score <=21:
        print(f"Dealern vann med {dealer.score} poäng ")
    elif dealer.score == player.score:
        print(f"Dealern vinner på lika som är {dealer.score} poäng ")
    else:
        print(f"{player.name} vinner med {player.score} poäng")
    
if __name__ == "__main__":
    play() # startar spelet
    

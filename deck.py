import random # importerar random-modulen

class Deck:
    def __init__(self) -> None:
        # korten med dess värden
        self.card_values: list[tuple[str, int]] = [
            ("2", 2), ("3", 3), ("4",4), ("5", 5), ("6", 6), ("7", 7),
            ("8", 8), ("9", 9), ("10", 10), ("knäckt", 11),
            ("dam", 12), ("kung", 13), ("ess", 14)
        ]
        
    def draw_card(self) -> tuple[str, int]:
        # Slumpar fram ett kort från kortleken och returnerar dess namn och värde
        return random.choice(self.card_values)
    
    
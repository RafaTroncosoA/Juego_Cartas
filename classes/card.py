class Card:

    def __init__( self , suit , point_val , string_val ):
        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")
    
    def valor_pinta(self):
        dict_pinta= {"spades":3 , "hearts":2 , "clubs":1, "diamonds":4}
        return dict_pinta[self.suit]

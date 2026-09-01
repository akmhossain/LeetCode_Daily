class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter, number = coordinates[0], int(coordinates[1])
        if number % 2 == 1:
            start = 'black'
        else:
            start = 'white'
        
        # 97 - a
        letter_ascii = ord(letter)

        # 
        if letter_ascii % 2 == 1:
            if start == 'black':
                return False 
            else:
                return True
        else:
            if start == 'black':
                return True 
            else:
                return False
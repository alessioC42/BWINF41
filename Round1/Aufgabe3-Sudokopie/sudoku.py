class Sudoku:
    """
    Klasse zum Speichen von Sudokus mit Kommentar. 
    In diesem Kommentar werden die Mutationen des Sudokus zur späteren Ausgabe festgehalten.
    """
    def __init__(self, board, comment="") -> None:
        self.board = board
        self.comment = comment

    def printSudoku(self) -> None:
        """
        Ausgabe des Sudokus
        """
        for i in self.board:
            for number in i:
                print(number + " ", end="")
            print()

    def isNumberEqualTo(self, sudokuboard) -> bool:
        """
        Überprüft, ob die angegebene Sudoku.board Variable schematisch mit self.board übereinstimmt.
        Sollte dies der Fall sein wird ein formatierter String mit den "Nummerrelationen" zurückgegeben.
        """
        #objekt zum Speichen von Relationen
        keys = {"0": "0"}
        
        #Überprüfung von jedem Zahlenwert in self.board mit sudokuboard
        for x in range(0, 9):
            for y in range(0, 9):
                if self.board[x][y] in keys:
                    if not keys[self.board[x][y]] == sudokuboard[x][y]:
                        return {
                            "bool": False
                        }
                else:
                    keys[self.board[x][y]] = sudokuboard[x][y]

        #formatieren von keys für Ausgabe
        numberstr:str=""
        for i in range(1, 10):
            numberstr = numberstr+f"{str(i)}->{keys[str(i)]}; "

        return {
            "bool": True,
            "numbers": numberstr[:-2]
        }
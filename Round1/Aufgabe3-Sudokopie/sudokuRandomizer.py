from sudoku import Sudoku

class Randomizer:
    """
    Klasse zum Modifizieren/Mutieren von Sudoku objekten nach den Regeln der Aufgabenstellung im BWINF41-Aufgabe3.
    Alle Funktionen (außer rotate90degreeRight()) geben eine Liste mit allen möglichen Modifikatioenen/Mutationen zurück.
    """

    def getAllRotations(self, sudoku:Sudoku) -> list[Sudoku]:
        """
        Diese Funktion ermittelt alle möglichen Rotationen einens Sudokus und gibt diese zurück.
        """
        rotations = []
        rotations.append(Sudoku(self.rotate90degreeRight(sudoku), sudoku.comment+"\nRotated by 90°"))
        rotations.append(Sudoku(self.rotate90degreeRight(rotations[0]), sudoku.comment+"\nRotated by 180°"))
        rotations.append(Sudoku(self.rotate90degreeRight(rotations[1]), sudoku.comment+"\nRotated by 270°"))
        rotations.append(sudoku)
        return rotations

    def getAllMixedRowBlocks(self, sudoku:Sudoku) -> list[Sudoku]:
        s = sudoku.board
        Pvariations = [
            {"variation":[0, 1, 2, 3, 4, 5, 6, 7, 8], "comment": sudoku.comment},
            {"variation":[0, 1, 2, 6, 7, 8, 3, 4, 5], "comment": sudoku.comment + "\nMixed row blocks from 123 to 132"},
            {"variation":[3, 4, 5, 0, 1, 2, 6, 7, 8], "comment": sudoku.comment + "\nMixed row blocks from 123 to 213"},
            {"variation":[3, 4, 5, 6, 7, 8, 0, 1, 2], "comment": sudoku.comment + "\nMixed row blocks from 123 to 231"},
            {"variation":[6, 7, 8, 0, 1, 2, 3, 4, 5], "comment": sudoku.comment + "\nMixed row blocks from 123 to 312"},
            {"variation":[6, 7, 8, 3, 4, 5, 0, 1, 2], "comment": sudoku.comment + "\nMixed row blocks from 123 to 321"},
        ]
        variations = []

        for Pvariation in Pvariations:
            v = Pvariation["variation"]
            variation = []
            for i in range(0, 9):
                variation.append([s[v[i]][0], s[v[i]][1], s[v[i]][2], s[v[i]][3], s[v[i]][4], s[v[i]][5], s[v[i]][6], s[v[i]][7], s[v[i]][8]])
            variations.append(Sudoku(variation, Pvariation["comment"]))
        return variations

    def getAllMixedColumnBlocks(self, sudoku:Sudoku) -> list[Sudoku]:
        s = sudoku.board
        Pvariations = [
            {"variation":[0, 1, 2, 3, 4, 5, 6, 7, 8], "comment": sudoku.comment},
            {"variation":[0, 1, 2, 6, 7, 8, 3, 4, 5], "comment": sudoku.comment + "\nMixed column blocks from 123 to 132"},
            {"variation":[3, 4, 5, 0, 1, 2, 6, 7, 8], "comment": sudoku.comment + "\nMixed column blocks from 123 to 213"},
            {"variation":[3, 4, 5, 6, 7, 8, 0, 1, 2], "comment": sudoku.comment + "\nMixed column blocks from 123 to 231"},
            {"variation":[6, 7, 8, 0, 1, 2, 3, 4, 5], "comment": sudoku.comment + "\nMixed column blocks from 123 to 312"},
            {"variation":[6, 7, 8, 3, 4, 5, 0, 1, 2], "comment": sudoku.comment + "\nMixed column blocks from 123 to 321"},
        ]
        variations = []

        for Pvariation in Pvariations:
            v = Pvariation["variation"]
            variation = []
            for i in range(0, 9):
                variation.append([s[i][v[0]], s[i][v[1]], s[i][v[2]], s[i][v[3]], s[i][v[4]], s[i][v[5]], s[i][v[6]], s[i][v[7]], s[i][v[8]]])
            variations.append(Sudoku(variation, Pvariation["comment"]))
         
        return variations

    def getAllMixedInRowBlocksVariants(self, sudoku:Sudoku) -> list[Sudoku]:
        s = sudoku.board

        Pvariantions = ["012", "021", "102", "120", "201", "210"]
        variants = []

        for _1 in Pvariantions:
            comment = sudoku.comment
            _one = []
            for a in range(3):
                _one.append(s[int(_1[a])])
            
            if not _1 == "012":
                commentA = comment + "\nMixed in row block 1 from 012 to "+_1
            else: commentA = comment
            for _2 in Pvariantions:
                _two = _one.copy()
                for b in range(3):
                    _two.append(s[int(_2[b])+3])
                if not _2 == "012":
                    commentB = commentA + "\nMixed in row block 2 from 012 to "+_2
                else: commentB = commentA
                for _3 in Pvariantions:
                    _tree = _two.copy()
                    for c in range(3):
                        _tree.append(s[int(_3[c])+6])
                   
                    if not _3 == "012":
                        commentC = commentB + "\nMixed in row block 3 from 012 to "+_3
                    else: commentC = commentB

                    variants.append(Sudoku(_tree, commentC))
        return variants

    def getAllMixedInColumnBlocksVariants(self, sudoku:Sudoku) -> list[Sudoku]:
        inrowvariants = self.getAllMixedInRowBlocksVariants(Sudoku(self.rotate90degreeRight(sudoku), sudoku.comment))

        variants = []
        for i in inrowvariants:
            board = self.rotate90degreeLeft(i)
            newcommentpart = i.comment.replace(sudoku.comment, "")
            comment = sudoku.comment + newcommentpart.replace("in row block", "in column block")
            variants.append(Sudoku(board, comment))
        return variants

    def rotate90degreeRight(self, sudoku:Sudoku) -> list:
        """
        Dreht ein Sudoku um 90° nach Rechts und gibt eine Sudoku.board variable zurück.
        """
        s = sudoku.board
        rotation = []
        for i in range(0, 9):
            rotation.append([s[8][i], s[7][i], s[6][i], s[5][i], s[4][i], s[3][i], s[2][i], s[1][i], s[0][i]])
        return rotation
    
    def rotate90degreeLeft(self, sudoku:Sudoku) -> list:
        """
        Dreht ein Sudoku um 90° nach Links und gibt eine Sudoku.board variable zurück.
        """

        s = sudoku.board
        rotation = []
        for i in range(8, -1, -1):
            rotation.append([s[0][i], s[1][i], s[2][i], s[3][i], s[4][i], s[5][i], s[6][i], s[7][i], s[8][i]])
        return rotation


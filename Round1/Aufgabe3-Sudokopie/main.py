from sudoku import Sudoku
from sudokuRandomizer import Randomizer

#verwendung von sys.argv zur Parameterübergabe
from sys import argv

def main():
    #Klasse zum modifizieren von Sudokus
    ramdomizer = Randomizer() 

    #Datei lesen und in Zeilen aufteilen
    filelines = open(argv[1], "r").read().splitlines()

    sudokuraw1 = filelines[0:9]#oberes Sudoku
    sudokuraw2 = filelines[10:19]#unteres Sudoku

    #lesen von Sudoku1
    for index in range(0, 9):
        sudokuraw1[index] = sudokuraw1[index].split(" ")

    #lesen von Sudoku2
    for index in range(0, 9):
        sudokuraw2[index] = sudokuraw2[index].split(" ")

    sudoku1 = Sudoku(sudokuraw1)
    sudoku2 = Sudoku(sudokuraw2)

    #Alle möglichen Mutationen von sudoku1 mit sudoku2 vergleichen und bei Übereinstimmung ausgeben
    variants:int=1
    for a in (ramdomizer.getAllMixedInRowBlocksVariants(sudoku1)):
        for b in (ramdomizer.getAllMixedInColumnBlocksVariants(a)):
            for c in (ramdomizer.getAllMixedColumnBlocks(b)):
                for d in (ramdomizer.getAllMixedRowBlocks(c)):
                    for e in (ramdomizer.getAllRotations(d)):
                        #überprüfung der Zahlen im Sudoku
                        num = e.isNumberEqualTo(sudoku2.board)
                        if (num["bool"]):
                            print("----"+str(variants)+"----", end="")
                            print(e.comment)
                            print("number relations: "+str(num["numbers"]))
                            variants+=1


if __name__ == "__main__":
    main()
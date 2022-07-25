def getFile(piece, lst):
    file = int()
    for i in range(8):
        if piece in lst[i]:
            file = i
    return file


def getRank(piece, lst):
    rank = int()
    for i in range(8):
        for e in range(8):
            if lst[i][e] == piece:
                rank = e
    return rank


def getCoords(piece, lst):
    return getRank(piece, lst), getFile(piece, lst)


class Knight:
    """ru21: right two up one, ld12: left one two down, etc."""

    def ru21(self, lst, n=1):
        """Checks color of destination tile to determine whether a move
        there is legal"""
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if (white(lst[getFile(self, lst) - 1][getRank(self, lst) + 2])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst) + 2] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (black(lst[getFile(self, lst) + 1][getRank(self, lst) - 2])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst) - 2] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def ru12(self, lst, n=1):
        """Checks color of destination tile to determine whether a move
        there is legal"""
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if (white(lst[getFile(self, lst) - 2][getRank(self, lst) + 1])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 2][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (black(lst[getFile(self, lst) + 2][getRank(self, lst) - 1])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 2][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def lu21(self, lst, n=1):
        """Checks color of destination tile to determine whether a move
        there is legal"""
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if (white(lst[getFile(self, lst) - 1][getRank(self, lst) - 2])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst) - 2] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (black(lst[getFile(self, lst) + 1][getRank(self, lst) + 2])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst) + 2] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def lu12(self, lst, n=1):
        """Checks color of destination tile to determine whether a move
        there is legal"""
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if (white(lst[getFile(self, lst) - 2][getRank(self, lst) - 1])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 2][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (black(lst[getFile(self, lst) + 2][getRank(self, lst) + 1])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 2][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def rd21(self, lst, n=1):
        """Checks color of destination tile to determine whether a move
        there is legal"""
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if (white(lst[getFile(self, lst) + 1][getRank(self, lst) + 2])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst) + 2] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (black(lst[getFile(self, lst) - 1][getRank(self, lst) - 2])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst) - 2] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def rd12(self, lst, n=1):
        """Checks color of destination tile to determine whether a move
        there is legal"""
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if (white(lst[getFile(self, lst) + 2][getRank(self, lst) + 1])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 2][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (black(lst[getFile(self, lst) - 2][getRank(self, lst) - 1])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 2][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def ld21(self, lst, n=1):
        """Checks color of destination tile to determine whether a move
        there is legal"""
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if (white(lst[getFile(self, lst) + 1][getRank(self, lst) - 2])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst) - 2] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (black(lst[getFile(self, lst) - 1][getRank(self, lst) + 2])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst) + 2] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def ld12(self, lst, n=1):
        """Checks color of destination tile to determine whether a move
        there is legal"""
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if (white(lst[getFile(self, lst) + 2][getRank(self, lst) - 1])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 2][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (black(lst[getFile(self, lst) - 2][getRank(self, lst) + 1])):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 2][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def __str__(self):
        return "4"
    # third from king leftward


class Bishop:
    """Right up, left up, right down, left down,  n-many tiles"""

    def ru(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces from a bishop to a piece 
        above and to the right to determine whether a move is legal. If so, 
        the bishop object replaces the object at the new rank and file 
        indices given by adding or subtracting the "n" arg (depending on its 
        color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank + i] != 10:
                    collision_lst.append(lst[init_file - i][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and
                  not (collision_lst[0] == lst[init_file - n][init_rank + n])
            ):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank + i] != 10:
                    collision_lst.append(lst[init_file + i][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank - n], self):
                print("Please select a different move")
            elif (collision_count == 1 and
                  not (collision_lst[0] == lst[init_file + n][init_rank - n])
            ):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst) - n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def lu(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces to the left of and above 
        a bishop to determine whether a move is legal. If so, the bishop 
        object replaces the object at the new rank and file indices given by
        adding or subtracting the "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank - i] != 10:
                    collision_lst.append(lst[init_file - i][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank - n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank - n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst) - n] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file + i][init_rank + i] != 10:
                    collision_lst.append(lst[init_file + i][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file + n][init_rank + n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def rd(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces from a bishop to a piece 
        above and below to determine whether a move is legal. If so, the
        bishop object replaces the object at the new rank and file indices 
        given by adding or subtracting the "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file + i][init_rank + i] != 10:
                    collision_lst.append(lst[init_file + i][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file + n][init_rank + n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank - i] != 10:
                    collision_lst.append(lst[init_file - i][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank - n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank - n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst) - n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def ld(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces from a bishop to a piece 
        below and to the left to determine whether a move is legal. If so, 
        the bishop object replaces the object at the new rank and file 
        indices given by adding or subtracting the "n" arg (depending on 
        its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file + i][init_rank - i] != 10:
                    collision_lst.append(lst[init_file + i][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank - n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file + n][init_rank - n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst) - n] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank + i] != 10:
                    collision_lst.append(lst[init_file - i][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank + n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def __str__(self):
        return "3"
    # second from king leftward


class Pawn:

    def forward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if (lst[getFile(self, lst) - 1][getRank(self, lst)] != 10):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (lst[getFile(self, lst) + 1][getRank(self, lst)] != 10):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def forwardTwo(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if (lst[getFile(self, lst) - 2][getRank(self, lst)] != 10 or getFile(self, lst) != 6):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 2][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (lst[getFile(self, lst) + 2][getRank(self, lst)] != 10 or getFile(self, lst) != 1):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 2][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def rightCapture(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        """checks whether the tile to the right and above a pawn is 
        empty or harbors a piece of the same color, in which case no move 
        will be made. Else, the pawn will move to the tile"""
        if white(self):
            if (white(lst[getFile(self, lst) - 1][getRank(self, lst) + 1]) or lst[getFile(self, lst) - 1][
                getRank(self, lst) + 1] == 10):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (black(lst[getFile(self, lst) + 1][getRank(self, lst) - 1]) or lst[getFile(self, lst) + 1][
                getRank(self, lst) - 1] == 10):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def leftCapture(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        """checks whether the tile to the left and above a pawn is empty or
        harbors a piece of the same color, in which case no move will be 
        made. Else, the pawn will move to the tile"""
        if white(self):
            if (white(lst[getFile(self, lst) - 1][getRank(self, lst) - 1]) or lst[getFile(self, lst) - 1][
                getRank(self, lst) - 1] == 10):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if (black(lst[getFile(self, lst) + 1][getRank(self, lst) + 1]) or lst[getFile(self, lst) + 1][
                getRank(self, lst) + 1] == 10):
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def __str__(self):
        return "6"


class Rook:
    """Rook forward, backward, leftward, and rightward n-many tiles"""

    def forward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces in front of a rook to 
        determine whether a move is legal. If so, the rook object replaces 
        the object at the new file index given by adding or subtracting the
        "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank] != 10:
                    collision_lst.append(lst[init_file - i][init_rank])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file + i][init_rank] != 10:
                    collision_lst.append(lst[init_file + i][init_rank])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file + n][init_rank])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def backward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces behind a rook to 
        determine whether a move is legal. If so, the rook object replaces 
        the object at the new file index given by adding or subtracting the 
        "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file + i][init_rank] != 10:
                    collision_lst.append(lst[init_file + i][init_rank])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file + n][init_rank])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank] != 10:
                    collision_lst.append(lst[init_file - i][init_rank])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def leftward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces to the left of a rook to 
        determine whether a move is legal. If so, the rook object replaces 
        the object at the new rank index given by adding or subtracting the 
        "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file][init_rank - i] != 10:
                    collision_lst.append(lst[init_file][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file][init_rank + i] != 10:
                    collision_lst.append(lst[init_file][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file][init_rank + n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def rightward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces to the right of a rook to 
        determine whether a move is legal. If so, the rook object replaces 
        the object at the new rank index given by adding or subtracting the 
        "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file][init_rank + i] != 10:
                    collision_lst.append(lst[init_file][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file][init_rank + n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file][init_rank - i] != 10:
                    collision_lst.append(lst[init_file][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file][init_rank - n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file][init_rank - n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) - n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def __str__(self):
        return "5"
    # king is one, rook is fourth piece from the king leftward


class Queen:

    def forward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces in front of a queen to 
        determine whether a move is legal. If so, the queen object replaces 
        the object at the new file index given by adding or subtracting the 
        "n" arg (depending on its color)"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank] != 10:
                    collision_lst.append(lst[init_file - i][init_rank])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file + i][init_rank] != 10:
                    collision_lst.append(lst[init_file + i][init_rank])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file + n][init_rank])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def backward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces behind a queen to 
        determine whether a move is legal. If so, the queen object replaces 
        the object at the new file index given by adding or subtracting the 
        "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file + i][init_rank] != 10:
                    collision_lst.append(lst[init_file + i][init_rank])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file + n][init_rank])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank] != 10:
                    collision_lst.append(lst[init_file - i][init_rank])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def leftward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces to the left of a queen to
        determine whether a move is legal. If so, the queen object replaces 
        the object at the new rank index given by adding or subtracting the 
        "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file][init_rank - i] != 10:
                    collision_lst.append(lst[init_file][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file][init_rank + i] != 10:
                    collision_lst.append(lst[init_file][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file][init_rank + n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def rightward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces to the right of a queen 
        to determine whether a move is legal. If so, the queen object 
        replaces the object at the new rank index given by adding or 
        subtracting the "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file][init_rank + i] != 10:
                    collision_lst.append(lst[init_file][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file][init_rank + n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file][init_rank - i] != 10:
                    collision_lst.append(lst[init_file][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file][init_rank - n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file][init_rank - n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) - n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def ru(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces from a queen to a piece
        above and to the right to determine whether a move is legal. If so, 
        the queen object replaces the object at the new rank and file 
        indices given by adding or subtracting the "n" arg (depending on its
        color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank + i] != 10:
                    collision_lst.append(lst[init_file - i][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank + n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank + i] != 10:
                    collision_lst.append(lst[init_file + i][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank - n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file + n][init_rank - n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst) - n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def lu(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces to the left of and above 
        a queen to determine whether a move is legal. If so, the queen 
        object replaces the object at the new rank and file indices given 
        by adding or subtracting the "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank - i] != 10:
                    collision_lst.append(lst[init_file - i][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank - n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank - n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst) - n] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file + i][init_rank + i] != 10:
                    collision_lst.append(lst[init_file + i][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file + n][init_rank + n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def rd(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces from a queen to a piece 
        above and below to determine whether a move is legal. If so, the 
        queen object replaces the object at the new rank and file indices 
        given by adding or subtracting the "n" arg (depending on its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file + i][init_rank + i] != 10:
                    collision_lst.append(lst[init_file + i][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank + n], self):
                print("Please select a different move")
            elif (
                    collision_count == 1 and
                    not (collision_lst[0] == lst[init_file + n][init_rank + n])
            ):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank - i] != 10:
                    collision_lst.append(lst[init_file - i][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank - n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank - n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst) - n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def ld(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        collision_lst = []
        """checks the presence and color of pieces from a queen to a piece 
        below and to the left to determine whether a move is legal. If so, 
        the queen object replaces the object at the new rank and file 
        indices given by adding or subtracting the "n" arg (depending on 
        its color"""
        if white(self):
            for i in range(1, n + 1):
                if lst[init_file + i][init_rank - i] != 10:
                    collision_lst.append(lst[init_file + i][init_rank - i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file + n][init_rank - n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file + n][init_rank - n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) + n][getRank(self, lst) - n] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            for i in range(1, n + 1):
                if lst[init_file - i][init_rank + i] != 10:
                    collision_lst.append(lst[init_file - i][init_rank + i])
            collision_count = len(collision_lst)
            if collision_count == 1 and sameColor(lst[init_file - n][init_rank + n], self):
                print("Please select a different move")
            elif (collision_count == 1 and not (collision_lst[0] == lst[init_file - n][init_rank + n])):
                print("Please select a different move")
            elif collision_count > 1:
                print("Please select a different move")
            else:
                lst[getFile(self, lst) - n][getRank(self, lst) + n] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def __str__(self):
        return "2"
    # adjacent to king from left


class King:
    """methods inspired by those of the rook and bishop, but n is set to a
    constant 1"""

    def forward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if white(lst[getFile(self, lst) - 1][getRank(self, lst)]):
                print("Please select another move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if black(lst[getFile(self, lst) + 1][getRank(self, lst)]):
                print("Please select another move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def backward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if white(lst[getFile(self, lst) + 1][getRank(self, lst)]):
                print("Please select another move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if black(lst[getFile(self, lst) - 1][getRank(self, lst)]):
                print("Please select another move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst)] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def leftward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if white(lst[getFile(self, lst)][getRank(self, lst) - 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if black(lst[getFile(self, lst)][getRank(self, lst) + 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def rightward(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if white(lst[getFile(self, lst)][getRank(self, lst) + 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if black(lst[getFile(self, lst)][getRank(self, lst) - 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst)][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def ru(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if white(lst[getFile(self, lst) - 1][getRank(self, lst) + 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst - 1)][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if black(lst[getFile(self, lst) + 1][getRank(self, lst) - 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def lu(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if white(lst[getFile(self, lst) - 1][getRank(self, lst) - 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst - 1)][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if black(lst[getFile(self, lst) + 1][getRank(self, lst) + 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def rd(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if white(lst[getFile(self, lst) + 1][getRank(self, lst) + 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if black(lst[getFile(self, lst) - 1][getRank(self, lst) - 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def ld(self, lst, n=1):
        lst = internal_board
        init_rank = getRank(self, lst)
        init_file = getFile(self, lst)
        if white(self):
            if white(lst[getFile(self, lst) + 1][getRank(self, lst) - 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst) + 1][getRank(self, lst) - 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()
        else:
            if black(lst[getFile(self, lst) - 1][getRank(self, lst) + 1]):
                print("Please select another move")
            else:
                lst[getFile(self, lst) - 1][getRank(self, lst) + 1] = self
                lst[init_file][init_rank] = 10
                updateBoard()

    def __str__(self):
        return "1"


# instantiates all pieces
nw1, nw2, nb1, nb2 = Knight(), Knight(), Knight(), Knight()

rw1, rw2, rb1, rb2 = Rook(), Rook(), Rook(), Rook()

bw1, bw2, bb1, bb2 = Bishop(), Bishop(), Bishop(), Bishop()

kw1, kb1 = King(), King()

qw1, qb1 = Queen(), Queen()

pw1, pw2, pw3, pw4, pw5, pw6, pw7, pw8 = Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn()

pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8 = Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn()

# the board manipulated by methods and such
internal_board = [
    [rb2, nb2, bb2, kb1, qb1, bb1, nb1, rb1],
    [pb8, pb7, pb6, pb5, pb4, pb3, pb2, pb1],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [pw1, pw2, pw3, pw4, pw5, pw6, pw7, pw8],
    [rw1, nw1, bw1, qw1, kw1, bw2, nw2, rw2]
]

# This list is what is printed to the screen after updateBoard() is called
# It represents the updated board
user_board = [
    [int(rb2.__str__().__str__() * 2), int(nb2.__str__().__str__() * 2), int(bb2.__str__().__str__() * 2),
     int(kb1.__str__().__str__() * 2), int(qb1.__str__().__str__() * 2), int(bb1.__str__().__str__() * 2),
     int(nb1.__str__().__str__() * 2), int(rb1.__str__().__str__() * 2)],
    [int(pb8.__str__().__str__() * 2), int(pb7.__str__().__str__() * 2),
     int(pb6.__str__().__str__() * 2), int(pb5.__str__().__str__() * 2),
     int(pb4.__str__().__str__() * 2), int(pb3.__str__().__str__() * 2),
     int(pb2.__str__().__str__() * 2), int(pb1.__str__().__str__() * 2)],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [int(pb1.__str__().__str__() + "9"), int(pb2.__str__().__str__() + "9"), int(pb3.__str__().__str__() + "9"),
     int(pb4.__str__().__str__() + "9"), int(pb5.__str__().__str__() + "9"), int(pb6.__str__().__str__() + "9"),
     int(pb7.__str__().__str__() + "9"), int(pb8.__str__().__str__() + "9")],
    [int(rw1.__str__().__str__() + "9"), int(nw1.__str__().__str__() + "9"),
     int(bw1.__str__().__str__() + "9"), int(qw1.__str__().__str__() + "9"), int(kw1.__str__().__str__() + "9"),
     int(bw2.__str__().__str__() + "9"), int(nw2.__str__().__str__() + "9"), int(rw2.__str__().__str__() + "9")]
]
# sets up a dictionary storing the coordinates of every piece in a
# dictionary.
positions = dict()
for file in internal_board:
    for piece in file:
        if not isinstance(piece, int):
            positions[piece] = getCoords(piece, internal_board)

piece_lst = [
    pw1, pw2, pw3, pw4, pw5, pw6, pw7, pw8, rw1, rw2, nw1, nw2, kw1, qw1, bw1, bw2, pb1, pb2, pb3, pb4, pb5, pb6, pb7,
    pb8, rb1, rb2, nb1, nb2, kb1, qb1, bb1, bb2
]
# maps strings to pieces
string_to_piece_map = {
    "pw1": pw1, "pw2": pw2, "pw3": pw3, "pw4": pw4, "pw5": pw5, "pw6": pw6,
    "pw7": pw7, "pw8": pw8, "rw1": rw1, "rw2": rw2, "nw1": nw1, "nw2": nw2,
    "kw1": kw1, "qw1": qw1, "bw1": bw1, "bw2": bw2, "pb1": pb1, "pb2": pb2,
    "pb3": pb3, "pb4": pb4, "pb5": pb5, "pb6": pb6, "pb7": pb7, "pb8": pb8,
    "rb1": rb1, "rb2": rb2, "nb1": nb1, "nb2": nb2, "kb1": kb1, "qb1": qb1,
    "bb1": bb1, "bb2": bb2
}

# maps pieces to strings
piece_to_string_map = {}
for k, v in string_to_piece_map.items():
    piece_to_string_map[v] = k


# determines whether a piece is white by seeing at what index it lies in
# piece_lst, similarly for black()
def white(piece):
    count = 0
    for i in range(len(piece_lst)):
        if i <= 15 and piece_lst[i] is piece:
            count += 1
    return count > 0


def black(piece):
    count = 0
    for i in range(len(piece_lst)):
        if i > 15 and piece_lst[i] is piece:
            count += 1
    return count > 0


def sameColor(piece1, piece2):
    return (black(piece1) and black(piece2)) or (white(piece1) and white(piece2))


def diffColor(piece1, piece2):
    return (black(piece1) and white(piece2)) or (white(piece1) and black(piece2))


# updates the board that the user sees by mutating the items in
# internal_board. Specifically white pieces' representations are suffixed
# with "9" and black pieces' representations are doubled
def updateBoard(lst=internal_board):
    user_board = [
        [int(e.__str__().__str__() * 2) if black(e)
         else int(e.__str__().__str__() + "9") if white(e) else e for e in i]
        for i in lst
    ]
    for i in user_board:
        print(i)
    print("\n")


def init():
    for i in user_board:
        print(i)
    print("\n")


# instead of taking user input and returning a string representation of a
# piece to be displayed to the user, this function takes algebraic coords
# in the form of a string and returns the piece at that location
def getPieceFromCoords(coords_str):
    if len(coords_str) != 2:
        print("Invalid coordinates")
    else:
        char_map = {
            "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7
        }
        rank_repr = coords_str[0]
        try:
            rank = char_map[rank_repr]
        except:
            print("Invalid rank")
        inverse_file = int(coords_str[1]) - 1
        # file accounts for zero indexing and the fact that the file in a list (row)
        # is reverse, hence the 7-inverse_file
        file = 7 - inverse_file
        piece = internal_board[file][rank]
        if isinstance(piece, int):
            print("There is no piece at this coordinate")
        else:
            return piece


# takes user input coordinates and prints a string representation of the piece
# at this location
def printPieceFromCoords():
    coords_repr = input("Coordinates in algebraic notation?\n")
    if len(coords_repr) != 2:
        print("Invalid coordinates")
    else:
        print(piece_to_string_map[getPieceFromCoords(coords_repr)])


# user enters a string consisting of two initial chars representing
# coordinates in algebraic chess notation, the last char
# is the number of tiles moved, and the middle string represents the
# particular move.
def user_input(move):
    # allows the user to ask at any time the identity of a piece at any
    # location of the board
    if move == "?":
        printPieceFromCoords()
    else:
        coords = move[:2]
        move_type = move[2:-1]
        n = move[-1]
        piece = getPieceFromCoords(coords)

        if move_type == "forward":
            try:
                piece.forward(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "forwardtwo":
            try:
                piece.forwardTwo(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "backward":
            try:
                piece.backward(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "leftward":
            try:
                piece.leftward(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "rightward":
            try:
                piece.rightward(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "ru" or move_type == "rightup":
            try:
                piece.ru(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "lu" or move_type == "leftup":
            try:
                piece.lu(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "rd" or move_type == "rightdown":
            try:
                piece.rd(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "ld" or move_type == "leftdown":
            try:
                piece.ld(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "rightcapture":
            try:
                piece.rightCapture(internal_board)
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "leftcapture":
            try:
                piece.leftCapture(internal_board)
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "ru21" or move_type == "rightup21":
            try:
                piece.ru21(internal_board)
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "ru12" or move_type == "rightup12":
            try:
                piece.ru12(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "lu21" or move_type == "leftup21":
            try:
                piece.lu21(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "lu12" or move_type == "leftup12":
            try:
                piece.lu12(internal_board, int(n))
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "rd21" or move_type == "rightdown21":
            try:
                piece.rd21(internal_board)
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "rd12" or move_type == "rightdown12":
            try:
                piece.rd12(internal_board)
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "ld21" or move_type == "leftdown21":
            try:
                piece.ld21(internal_board)
            except:
                print("Invalid move. Please select a different one.\n")
        elif move_type == "ld12" or move_type == "leftdown12":
            try:
                piece.ld12(internal_board)
            except:
                print("Invalid move. Please select a different one.\n")

def play():
    instructions = "Hello! Before you is the visually stunning board on which you will play. White pieces end in the digit 9 and black pieces are doubled digits.\n\nPawns begin with 6, rooks with 5, knights with 4, bishops with 3, queens with 2, and kings with 1. Tiles on the board labeled '10' are considered empty. \n\nHere is notation to move a piece:\n[rank][file][move type][#tiles moved]\nRank and File are included to indicate the position of the piece the player desires to move. Number of tiles moved indicates the number of tiles moved, and in move types (to be listed exhaustively below) such as a knight jump or a pawn step forward, it must be explicitly indicated as '1'. Here are all possible move types:\n\n'leftward': moves a piece to its left\n'rightward': moves a piece to its right\n'forward': moves a piece forward\n'backward': moves a piece backward\n'ru' or 'rightup': moves a piece to the right and ahead an equal amount\n'lu' or 'leftup': moves a piece to the left and ahead an equal amount\n'rd' or 'rightdown': moves a piece to the right and behind an equal amount\n'ld' or 'leftdown': moves a piece to the left and behind an equal amount\n'leftcapture': makes a pawn capture a piece to the left and ahead of it\n'rightcapture': makes a pawn capture a piece to the right and ahead of it\n'forwardtwo': moves a pawn forward two tiles\n'ru21' or 'rightup21': moves a knight to the right two tiles and ahead one tile\n'lu21' or 'leftup21': moves a knight to the left two tiles and ahead one tile\n'rd21' or 'rightdown21': moves a knight to the right two tiles and behind one tile\n'ld21' or 'leftdown21': moves a knight to the left two tiles and behind one tile\n'ru12' or 'rightup12': moves a knight to the right one tile and ahead two tiles\n'lu12' or 'leftup12': moves a knight to the left one tile and ahead two tiles\n'rd12' or 'rightdown12': moves a knight to the right one tile and behind two tiles\n'ld12' or 'leftdown12': moves a knight to the left one tile and behind two tiles\n\nAn example command would be b1ru121 to move the starting knight to c3 from b1 or d7forwardtwo1 to move the starting pawn at d7 to d5.\n\nCheckmate detection and castling are currently not available, but I hope you will enjoy in the meantime. Enter 'Done' or 'Finished' to indicate that the game is finished. Enter '?' to inquire the identity of the piece at given coordinates\n\n" 
    give_instructions = input(
        "Press enter to skip instructions, else enter any key combination.\n"
        )
    if give_instructions != "":
        print(instructions)
    move_prompt = input("Move?\n")
    while move_prompt != "Done" and move_prompt != "Finished":
        user_input(move_prompt)
        move_prompt = input("Move?\n") 
        
        
init()
play()

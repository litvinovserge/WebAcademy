class TicTacToe:
    """
    Main Logic class - для игры крестики-нолики. Работает только с игровой сеткой NxN
    """

    def __init__(self, current_game, win_conditions=3):
        self.current_game = current_game
        self.win_conditions = win_conditions
        self.go()

    def go(self):
        return any((
            self.horizontal_check(),
            self.vertical_check(),
            self.diagonal_main_check(),
            self.diagonal_reverse_check()
        ))

    # 0 - определяем условия для победы
    def is_winner(self, current_result):
        return any((
            'x' * self.win_conditions in current_result,
            'o' * self.win_conditions in current_result
        ))

    # 1 - поиск победителя по горизонтали -  по линиям
    def horizontal_check(self):
        for line in self.current_game:
            current_line = ''
            for element in line:
                current_line += element
            if self.is_winner(current_line):
                return True

    # 2 - поиск победителя по вертикали - по столбцам
    def vertical_check(self):
        for line in range(len(self.current_game)):
            current_column = ''
            for column in range(len(self.current_game[line])):
                current_column += self.current_game[column][line]
            if self.is_winner(current_column):
                return True

    # 3 - поиск победителя по главной диагонали
    def diagonal_main_check(self):
        current_diagonal = ''
        for i in range(len(self.current_game)):
            current_diagonal += self.current_game[i][i]
        if self.is_winner(current_diagonal):
            return True

    # 4 - поиск победителя по обратной диагонали
    def diagonal_reverse_check(self):
        current_diagonal = ''
        for i in range(len(self.current_game)):
            current_diagonal += self.current_game[-i - 1][i]
        if self.is_winner(current_diagonal):
            return True


if __name__ == '__main__':
    test = [
        ['x', 'q', 's', 'x', 'q'],
        ['a', 'x', 'o', 'x', ''],
        ['x', '', 'x', 'i', ''],
        ['w', 'x', '', 'x', ''],
        ['x', '', '', '', '']
    ]
    game = TicTacToe(test, 5)
    print(game.go())

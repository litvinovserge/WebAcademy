__author__ = 'Sergey Litvinov'

import sys
import logic_v1
from PyQt5 import QtWidgets, QtGui, QtCore


class TicTacToeGUI(QtWidgets.QMainWindow):
    """
    GUI class на основе PyQT - для игры крестики-нолики
    """

    # 0 - определение базовых параметров для окна игры
    QtWidgets.QApplication.setFont(QtGui.QFont('Arial', 18))
    GAME_TITLE = 'TicTacToe v.1'
    GAME_ICON_PATH = r'pictures\favicon.png'
    BTN_SPACES = 15  # отступы от краев окна
    BTN_SIZE = 100  # ширина/высота для квадратных кнопок
    GRID_OPTIONS = [
        'Select the grid size',
        '3 x 3', '4 x 4', '5 x 5', '6 x 6', '7 x 7', '8 x 8', '9 x 9'
    ]  # варианты размера сетки для combobox

    def __init__(self, grid_size=3):
        super().__init__()
        self.grid_size = grid_size  # размер сетки для игры
        self.moves_counter = 0  # счетчик ходов
        self.game_history = [[''] * self.grid_size for i in range(self.grid_size)]  # буфер для истории всех ходов
        self.init_main_window()  # запуск инициализации главного окна
        self.init_buttons()  # запуск инициализации кнопок
        self.init_combobox()  # запуск инициализации кнопок
        self.show()

    # 1 - инициализация главного окна GUI
    def init_main_window(self):
        # параметры главного окна
        self.setWindowIcon(QtGui.QIcon(self.GAME_ICON_PATH))
        self.setWindowTitle(self.GAME_TITLE)
        self.statusBar().showMessage(f'It"s PLAYER "X" turn  ||  Total moves: {self.moves_counter}')
        self.setFixedWidth(self.BTN_SIZE * self.grid_size + self.BTN_SPACES * 2)
        self.setFixedHeight(self.BTN_SIZE * self.grid_size + self.BTN_SIZE * 1.6)

    # 2 - инициализация кнопок для окна GUI
    def init_buttons(self):
        # 2.1 - кнопки для поля игры
        self.btn_grid = [[None] * self.grid_size for i in range(self.grid_size)]
        yk = self.BTN_SIZE - 20
        for ay in range(self.grid_size):
            xk = 0
            for ax in range(self.grid_size):
                self.btn_grid[ay][ax] = QtWidgets.QPushButton('---', self)
                self.btn_grid[ay][ax].setObjectName(f'{ay}{ax}')
                self.btn_grid[ay][ax].setFixedHeight(self.BTN_SIZE)
                self.btn_grid[ay][ax].setFixedWidth(self.BTN_SIZE)
                self.btn_grid[ay][ax].move(xk + self.BTN_SPACES, yk)
                self.btn_grid[ay][ax].clicked.connect(self.btn_pressed)
                xk += self.BTN_SIZE
            yk += self.BTN_SIZE
        # 2.2 - кнопки для старта новой игры и выхода из игры
        self.btn_new_game = QtWidgets.QPushButton('New Game', self)
        self.btn_new_game.setObjectName('btn_new_game')
        self.btn_new_game.setFixedHeight(self.BTN_SIZE / 2)
        self.btn_new_game.setFixedWidth(self.BTN_SIZE * self.grid_size / 2)
        position = [self.BTN_SPACES, self.BTN_SIZE * self.grid_size + self.BTN_SIZE / 1.2]
        self.btn_new_game.move(position[0], position[1])
        self.btn_new_game.clicked.connect(self.btn_pressed)
        # 2.3 - кнопка для закрытия окна игры
        self.btn_close_game = QtWidgets.QPushButton('Close Game', self)
        self.btn_close_game.setObjectName('btn_close_game')
        self.btn_close_game.setFixedHeight(self.BTN_SIZE / 2)
        self.btn_close_game.setFixedWidth(self.BTN_SIZE * self.grid_size / 2)
        position = [self.BTN_SPACES + self.btn_new_game.width(), self.BTN_SIZE * self.grid_size + self.BTN_SIZE / 1.2]
        self.btn_close_game.move(position[0], position[1])
        self.btn_close_game.clicked.connect(self.btn_pressed)

    # 3 - инициализация combobox для окна GUI
    def init_combobox(self):
        self.cmb_box = QtWidgets.QComboBox(self)
        self.cmb_box.addItems(self.GRID_OPTIONS)
        self.cmb_box.setFixedHeight(self.BTN_SIZE / 2)
        self.cmb_box.setFixedWidth(self.BTN_SIZE * self.grid_size )
        self.cmb_box.move(self.BTN_SPACES, self.BTN_SPACES)
        self.cmb_box.currentIndexChanged.connect(self.cmb_box_pressed)

    # 4 - обрабатываем клики
    def btn_pressed(self):
        sender = self.sender()
        # 4.1 - обработка button "New Game"
        if self.btn_new_game.objectName() == sender.objectName():
            for ay in range(self.grid_size):
                for ax in range(self.grid_size):
                    self.moves_counter = 0
                    self.game_history = [[''] * self.grid_size for i in range(self.grid_size)]
                    self.statusBar().showMessage(f'It"s PLAYER "X" turn  ||  Total moves: {self.moves_counter}')
                    self.btn_grid[ay][ax].setEnabled(True)
                    self.btn_grid[ay][ax].setText('---')
        # 4.2 - обработка button "Close Game"
        elif self.btn_close_game.objectName() == sender.objectName():
            self.close()
        # 4.3 - обработка buttons - считывание ходов
        else:
            if self.moves_counter % 2 == 0:
                sender.setText('X')
                sender.setEnabled(False)
                self.moves_counter += 1
                self.game_history[int(sender.objectName()[0])][int(sender.objectName()[1])] = 'x'
                self.statusBar().showMessage(f'It"s PLAYER "O" turn  ||  Total moves: {self.moves_counter}')
                if logic_v1.TicTacToe(self.game_history, self.grid_size).go():
                    self.statusBar().showMessage(f'We have a winner! Congratulations to PLAYER "X"')
                    for y in range(self.grid_size):
                        for x in range(self.grid_size):
                            self.btn_grid[y][x].setEnabled(False)
            else:
                sender.setText('O')
                sender.setEnabled(False)
                self.moves_counter += 1
                self.game_history[int(sender.objectName()[0])][int(sender.objectName()[1])] = 'o'
                self.statusBar().showMessage(f'It"s PLAYER "X" turn  ||  Total moves: {self.moves_counter}')
                if logic_v1.TicTacToe(self.game_history, self.grid_size).go():
                    self.statusBar().showMessage(f'We have a winner! Congratulations to PLAYER "O"')
                    for y in range(self.grid_size):
                        for x in range(self.grid_size):
                            self.btn_grid[y][x].setEnabled(False)

    # 5 - обрабатываем combobox
    def cmb_box_pressed(self):
        sender = self.sender()
        print(sender.currentIndex())
        self.close()
        self.__init__(sender.currentIndex() + 2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    game1 = TicTacToeGUI()
    sys.exit(app.exec_())

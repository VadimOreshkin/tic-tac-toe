# Tic-Tac-Toe (Console Game)

## Description

A simple console-based Tic-Tac-Toe game for two players. The game is written in Python and runs entirely in the terminal. Players take turns entering cell numbers (1–9) to place their marks (`X` and `O`).

## Features

- Two-player mode (no AI)
- Input validation (prevents overwriting occupied cells and out-of-range moves)
- Automatic win detection (rows, columns, diagonals)
- Draw detection
- Option to exit the game at any time by entering `0`
- Clean console board display

## How to Play

1. The game starts with player `X`.
2. On your turn, enter a number from **1 to 9** corresponding to the cell where you want to place your mark.
3. The board layout with cell numbers:

```
|  1  |  2  |  3  |
|  4  |  5  |  6  |
|  7  |  8  |  9  |
```

4. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins.
5. If all 9 cells are filled without a winner, the game ends in a draw.
6. Enter `0` at any time to exit the game.

## Installation

```bash
# Clone the repository
git clone https://github.com/VadimOreshkin/tic-tac-toe.git

# Navigate to the project folder
cd tic-tac-toe

# Run the game (Python 3 required)
python tic_tac_toe.py
```

## Usage

Simply run the script and follow the on-screen prompts:

```bash
python tic_tac_toe.py
```

### Example Game Session

```
Добро пожаловать в игру "Крестики-нолики"!
Игрок X начинает!
Номера клеток: 1-9 (0 - выход из игры)
---------------------
|  1  |  2  |  3  |
---------------------
|  4  |  5  |  6  |
---------------------
|  7  |  8  |  9  |
---------------------

Игрок X. Введите номер поля (0 - выход): 5
Ход выполнен удачно!
---------------------
|  1  |  2  |  3  |
---------------------
|  4  |  X  |  6  |
---------------------
|  7  |  8  |  9  |
---------------------
...
```

## Code Structure

| Function | Description |
|----------|-------------|
| `draw_playingfield()` | Displays the current board state |
| `game_move(index, char)` | Places a player's mark on the board if the move is valid |
| `check_win()` | Checks if a player has won |
| `is_draw()` | Checks if the board is full (draw) |
| `start_game()` | Main game loop, handles turns and game flow |

## Customization

You can change the board size by modifying the `playingfield_size` variable (default is `3` for a 3×3 grid). Note that win combinations are hardcoded for 3×3 only.

```python
playingfield_size = 3   # Change to 4 for 4x4 (win logic won't work without additional changes)
```

## Requirements

- Python 3.x

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT © [Vadim Oreshkin]

---

# Крестики-нолики (консольная игра)

## Описание

Простая консольная игра «Крестики-нолики» для двух игроков. Игра написана на Python и полностью работает в терминале. Игроки по очереди вводят номера клеток (1–9), чтобы поставить свой знак (`X` или `O`).

## Возможности

- Режим для двух игроков (без ИИ)
- Проверка корректности ввода (защита от перезаписи занятых клеток и выхода за пределы поля)
- Автоматическое определение победы (строки, столбцы, диагонали)
- Определение ничьей
- Возможность выйти из игры в любой момент, набрав `0`
- Чистое отображение игрового поля в консоли

## Как играть

1. Игра начинается с игрока `X`.
2. В свой ход введите число от **1 до 9**, соответствующее клетке, куда хотите поставить свой знак.
3. Разметка поля с номерами клеток:

```
|  1  |  2  |  3  |
|  4  |  5  |  6  |
|  7  |  8  |  9  |
```

4. Побеждает тот, кто первым поставит три своих знака в ряд (по горизонтали, вертикали или диагонали).
5. Если все 9 клеток заполнены, а победителя нет — объявляется ничья.
6. Введите `0` в любой момент, чтобы выйти из игры.

## Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/VadimOreshkin/tic-tac-toe.git

# Перейдите в папку проекта
cd tic-tac-toe

# Запустите игру (требуется Python 3)
python tic_tac_toe.py
```

## Использование

Просто запустите скрипт и следуйте подсказкам на экране:

```bash
python tic_tac_toe.py
```

### Пример игровой сессии

```
Добро пожаловать в игру "Крестики-нолики"!
Игрок X начинает!
Номера клеток: 1-9 (0 - выход из игры)
---------------------
|  1  |  2  |  3  |
---------------------
|  4  |  5  |  6  |
---------------------
|  7  |  8  |  9  |
---------------------

Игрок X. Введите номер поля (0 - выход): 5
Ход выполнен удачно!
---------------------
|  1  |  2  |  3  |
---------------------
|  4  |  X  |  6  |
---------------------
|  7  |  8  |  9  |
---------------------
...
```

## Структура кода

| Функция | Описание |
|---------|----------|
| `draw_playingfield()` | Отображает текущее состояние поля |
| `game_move(index, char)` | Ставит знак игрока на поле, если ход допустим |
| `check_win()` | Проверяет, есть ли победитель |
| `is_draw()` | Проверяет, заполнено ли всё поле (ничья) |
| `start_game()` | Основной игровой цикл, управляет ходами и проверкой окончания игры |

## Настройка

Вы можете изменить размер поля, поменяв переменную `playingfield_size` (по умолчанию `3` для поля 3×3). Учтите, что выигрышные комбинации жёстко заданы только для 3×3.

```python
playingfield_size = 3   # При изменении на 4 логика победы работать не будет без доработки
```

## Требования

- Python 3.x

## Вклад в проект

Pull request'ы приветствуются. Для серьёзных изменений сначала откройте issue, чтобы обсудить, что вы хотите изменить.

## Лицензия

MIT © [Vadim Oreshkin]
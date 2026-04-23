# Количество клеток:
playingfield_size = 3

# Игровое поле:
playingfield = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_playingfield():
    """
    Функция отображает текущее состояние игрового поля в консоли.
    """
    print('-' * 19)  # Верхняя граница

    for i in range(playingfield_size):
        # Строка с символами (X, O или числами)
        print(f'|  {playingfield[i * 3]}  |  {playingfield[1 + i * 3]}  |  {playingfield[2 + i * 3]}  |')
        print('-' * 19)  # Нижняя граница строки


def game_move(index, char):
    """
    Функция выполняет ход игрока.
    Проверяет корректность ввода и свободна ли клетка.

    Args:
        index: номер клетки (1-9) введенный пользователем
        char: символ текущего игрока ('X' или 'O')

    Returns:
        True если ход успешен, False если ошибка ввода
    """
    try:
        index = int(index)
        # Проверка: номер от 1 до 9 и клетка свободна
        if index < 1 or index > 9 or playingfield[index - 1] in ('X', 'O'):
            return False
        playingfield[index - 1] = char
        return True
    except ValueError:
        # Если ввели не число (буквы, символы и т.д.)
        return False


def check_win():
    """
    Проверяет, есть ли победитель на игровом поле.

    Returns:
        'X' или 'O' если есть победитель,
        False если победителя нет
    """
    # Все возможные выигрышные комбинации (индексы клеток 0-8)
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикали
        (0, 4, 8), (2, 4, 6)  # Диагонали
    )

    for pos in win_combination:
        # Проверяем, все ли три клетки в комбинации заняты одним игроком
        if (playingfield[pos[0]] == playingfield[pos[1]] == playingfield[pos[2]]):
            return playingfield[pos[0]]  # Возвращаем символ победителя

    return False  # Победителя нет


def is_draw():
    """
    Проверяет, заполнено ли все поле (ничья).

    Returns:
        True если все клетки заняты, иначе False
    """
    return all(cell in ('X', 'O') for cell in playingfield)


def start_game():
    """
    Основная функция игры.
    Управляет ходом игры, переключением игроков и проверкой условий окончания.
    """
    current_player = 'X'  # Начинает игрок с крестиками
    step = 1  # Номер шага (счетчик ходов)

    print('Добро пожаловать в игру "Крестики-нолики"!')
    print('Игрок X начинает!')
    print('Номера клеток: 1-9 (0 - выход из игры)')
    draw_playingfield()

    while step < 10:
        # Получаем ход от текущего игрока
        index = input(f'\nИгрок {current_player}. Введите номер поля (0 - выход): ')

        # Проверка на выход из игры
        if index == '0':
            print('Игра завершена. До свидания!')
            return

        # Пытаемся сделать ход
        if game_move(index, current_player):
            print('Ход выполнен удачно!')
            draw_playingfield()

            # Проверяем победу
            winner = check_win()
            if winner:
                print(f'Выиграл {winner}!')
                return

            # Проверяем ничью (если поле заполнено и нет победителя)
            if is_draw():
                print('Игра окончена. Ничья!')
                return

            # Меняем игрока
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            step += 1
        else:
            print('Неверный номер! Повторите!')


# Запуск игры
draw_playingfield()
print('Вы в игре!')
start_game()
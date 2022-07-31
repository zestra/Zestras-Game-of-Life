from buttons import Pixel_Button


def simulation(Map):
    TILE_SIZE = 30
    top_left_x = 135
    top_left_y = 150
    height = 28
    width = 58

    new_Map = []
    for y in range(height):
        new_Map.append([])
        for x in range(width):
            new_Map[len(new_Map) - 1].append(0)

    row = 0
    column = 0
    for y in range(height):
        for x in range(width):
            # ___|_0_1_2_3_4_
            #  0 | 0 0 0 0 0
            #  1 | 1 1 1 1 0
            #  2 | 0 0 1 1 0
            #  3 | 0 0 0 1 0
            #  4 | 0 0 0 0 0

            # [y + 1][x - 1] [y + 1][x] [y + 1][x + 1]
            #   [y][x - 1]     [y][x]     [y][x + 1]
            # [y - 1][x - 1] [y - 1][x] [y - 1][x + 1]

            if row == 0:
                if column == 0:
                    # ___|_0_1_2_3_4_
                    #  0 | N ? X X X
                    #  1 | ? ? X X X
                    #  2 | X X X X X
                    #  3 | X X X X X
                    #  4 | X X X X X
                    Neighbour_sum = (Map[row + 1][column] + Map[row + 1][column + 1]) + \
                                    (Map[row][column + 1])
                elif column == (width - 1):
                    # ___|_0_1_2_3_4_
                    #  0 | X X X ? N
                    #  1 | X X X ? ?
                    #  2 | X X X X X
                    #  3 | X X X X X
                    #  4 | X X X X X
                    Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column]) + \
                                    (Map[row][column - 1])
                else:
                    # ___|_0_1_2_3_4_
                    #  0 | ? N N N ?
                    #  1 | ? ? ? ? ?
                    #  2 | X X X X X
                    #  3 | X X X X X
                    #  4 | X X X X X
                    Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column] + Map[row + 1][column + 1]) + \
                                    (Map[row][column - 1] + Map[row][column + 1])
            elif row == (height - 1):
                if column == 0:
                    # ___|_0_1_2_3_4_
                    #  0 | X X X X X
                    #  1 | X X X X X
                    #  2 | X X X X X
                    #  3 | ? ? X X X
                    #  4 | N ? X X X
                    Neighbour_sum = (Map[row][column + 1]) + \
                                    (Map[row - 1][column] + Map[row - 1][column + 1])
                elif column == (width - 1):
                    # ___|_0_1_2_3_4_
                    #  0 | X X X X X
                    #  1 | X X X X X
                    #  2 | X X X X X
                    #  3 | X X X ? ?
                    #  4 | X X X ? N
                    Neighbour_sum = (Map[row][column - 1]) + \
                                    (Map[row - 1][column - 1] + Map[row - 1][column])
                else:
                    # ___|_0_1_2_3_4_
                    #  0 | X X X X X
                    #  1 | X X X X X
                    #  2 | X X X X X
                    #  3 | ? ? ? ? ?
                    #  4 | ? N N N ?
                    Neighbour_sum = (Map[row][column - 1] + Map[row][column + 1]) + \
                                    (Map[row - 1][column - 1] + Map[row - 1][column] + Map[row - 1][column + 1])

            else:
                if column == 0:
                    # ___|_0_1_2_3_4_
                    #  0 | ? ? X X X
                    #  1 | N ? X X X
                    #  2 | N ? X X X
                    #  3 | N ? X X X
                    #  4 | ? ? X X X
                    Neighbour_sum = (Map[row + 1][column] + Map[row + 1][column + 1]) + \
                                    (Map[row][column + 1]) + \
                                    (Map[row - 1][column] + Map[row - 1][column + 1])
                elif column == (width - 1):
                    # ___|_0_1_2_3_4_
                    #  0 | X X X ? ?
                    #  1 | X X X ? N
                    #  2 | X X X ? N
                    #  3 | X X X ? N
                    #  4 | X X X ? ?
                    Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column]) + \
                                    (Map[row][column - 1]) + \
                                    (Map[row - 1][column - 1] + Map[row - 1][column])
                else:
                    # ___|_0_1_2_3_4_
                    #  0 | ? ? ? ? ?
                    #  1 | ? N N N ?
                    #  2 | ? N N N ?
                    #  3 | ? N N N ?
                    #  4 | ? ? ? ? ?
                    Neighbour_sum = (Map[row + 1][column - 1] + Map[row + 1][column] + Map[row + 1][column + 1]) + \
                                    (Map[row][column - 1] + Map[row][column + 1]) + \
                                    (Map[row - 1][column - 1] + Map[row - 1][column] + Map[row - 1][column + 1])

            if Map[row][column] == 1:
                if Neighbour_sum > 3 or Neighbour_sum < 2:
                    new_Map[row][column] = 0
                else:
                    new_Map[row][column] = Map[row][column]

            else:
                if Neighbour_sum == 3:
                    new_Map[row][column] = 1
                else:
                    new_Map[row][column] = Map[row][column]

            column += 1

        row += 1
        column = 0

    Map = new_Map
    return Map


def create_map(buttons):
    Map = []
    for row in buttons:
        Map.append([])
        for button in row:
            if button.code == 0:
                Map[len(Map) - 1].append(0)
            else:
                Map[len(Map) - 1].append(1)

    return Map
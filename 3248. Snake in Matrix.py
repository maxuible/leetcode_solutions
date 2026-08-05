
from typing import List

def finalPositionOfSnake(n: int, commands: List[str]) -> int:

    total_down = 0
    total_right = 0
    for command in commands:

        if command == "LEFT":
            total_right = total_right - 1
        elif command == "RIGHT":
            total_right = total_right + 1
        elif command == "DOWN":
            total_down = total_down + 1
        elif command == "UP":
            total_down = total_down - 1



    # print("total down: ", total_down)
    # print("total right: ", total_right)

    return (n * total_down) + total_right

print(finalPositionOfSnake(n = 2, commands = ["RIGHT","DOWN"]))
print(finalPositionOfSnake(n = 3, commands = ["DOWN","RIGHT","UP"]))
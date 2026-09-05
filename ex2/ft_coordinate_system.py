import math


def get_player_pos() -> tuple:
    while True:
        try:
            coordinate = input(
                "Enter new coordinates as floats in format 'x,y,z': ")
            coordinates = coordinate.split(",")

            if len(coordinates) != 3:
                print("Invalid syntax")
                continue

            x = float(coordinates[0])
            y = float(coordinates[1])
            z = float(coordinates[2])
            return (x, y, z)
        except ValueError as err:
            print(f"Error on parameter '{coordinates[1]}' : {err}")
            continue

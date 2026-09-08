import math


def get_player_pos() -> tuple:
    while True:
        coordinate = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        coordinates = coordinate.split(",")

        if len(coordinates) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(coordinates[0])
            y = float(coordinates[1])
            z = float(coordinates[2])
            return (x, y, z)
        except ValueError:
            for parts in coordinates:
                parts = parts.strip()
                try:
                    float(parts)
                except ValueError as err:
                    print(f"Error on parameter '{parts}': {err}")
                    break
            continue


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: x={pos1[0]}, y={pos1[1]}, z={pos1[2]}")
    print(
        f"Distance to center: {math.sqrt((pos1[0])**2 + (pos1[1])**2 + (pos1[2])**2):.4f}")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2 + (pos2[2]-pos1[2])**2):.4f}")

import random


def gen_player_achievements() -> set:
    achievements = ["First Steps", "Master Explorer", "Boss Slayer",
                    "Collector Supreme", "World Savior", "Speed Runner",
                    "Strategist", "Survivor", "Treasure Hunter", "Unstoppable",
                    "Untouchable", "Sharp Mind", "Crafting Genius",
                    "Hidden Path Finder"]

    count = random.randint(7, 12)
    select = random.sample(achievements, count)
    return set(select)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    Alice = gen_player_achievements()
    Bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")
    print()
    all_achievements = Alice.union(Bob, Charlie, Dylan)
    print(f"All distinct achievements: {all_achievements}")
    print()
    Common_achievements = Alice.intersection(Bob, Charlie, Dylan)
    print(f"Common achievements: {Common_achievements}")

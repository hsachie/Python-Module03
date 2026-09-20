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
    print()
    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Dylan, Charlie)}")
    print(f"Only Charlie has: {Charlie.difference(Alice, Bob, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Alice, Bob, Charlie)}")
    print()
    print(f"Alice is missing: {all_achievements.difference(Alice)}")
    print()
    print(f"Bob is missing: {all_achievements.difference(Bob)}")
    print()
    print(f"Charlie is missing: {all_achievements.difference(Charlie)}")
    print()
    print(f"Dylan is missing: {all_achievements.difference(Dylan)}")
    print()
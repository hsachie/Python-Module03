import random

if __name__ == "__main__":
	print("=== Game Data Alchemist ===")
	print()
	player = ['Alice', 'bob', 'Charlie', 'dylan', 
		   	'Emma', 'Gregory', 'john', 'kevin', 'Liam']
	print(f"Initial list of players: {player}")
	print()
	capitalized = [name.capitalize() for name in player]
	print(f"New list with all names capitalized: {capitalized}")
	print()
	already_capitalized = [name for name in player if name[0].isupper()]
	print(f"New list of capitalized names only: {already_capitalized}")
	print()
	scores = {name: random.randint(0, 1000) for name in capitalized}
	print(f"Score dict: {scores}")
	average = sum(scores.values()) / len(scores)
	print(f"Score average is {round(average, 2)}")
	high_scores = {name: score for name, score in scores.items() if score > average}
	print(f"High scores: {high_scores}")	
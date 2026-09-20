import typing
import random

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
	players = ["charlie", "dylan", "alice", "bob"]
	actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]
	while True:
		name = random.choice(players)
		action = random.choice(actions)
		yield (name, action)

def consume_event(events: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
	while len(events) > 0:
		index = random.randrange(len(events))
		yield events.pop(index)

if __name__ == "__main__":
	print("=== Game Data Stream Processor ===")
	events = gen_event()
	for i in range(1000):
		event = next(events)
		print(f"Event {i}: Player {event[0]} did action {event[1]}")

	event_list = []

	for _ in range(10):
		event_list.append(next(events))

	print(f"Built list of 10 events: {event_list}")

	for event in consume_event(event_list):
		print(f"Got event from list: {event}")
		print(f"Remains in list: {event_list}")
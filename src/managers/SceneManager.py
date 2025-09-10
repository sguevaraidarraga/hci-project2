from sys import stdin

class SceneManager:
	def __init__(self, scenes: dict):
		self.scenes = scenes

	def play_scene(self, start_id = 0):
		current_id = start_id
		while True:
			scene = self.scenes[current_id]
			print("\n" + scene.text)

			# audio

			if not scene.options:
				break

			print("\nOpciones:")
			for i, option in enumerate(scene.options, 1):
				print(f"{i}. {option["text"]}")

			choice = int(stdin.readline())-1
			current_id = scene.options[choice]["next_id"]
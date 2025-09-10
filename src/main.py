from utils.Constants import SCENE_PATH
from utils.FileManager import FileManager
from managers.SceneManager import SceneManager

def main():
	scenes = FileManager.load_scenes_from_json(SCENE_PATH)
	manager = SceneManager(scenes)
	manager.play_scene(start_id = 0)

main()
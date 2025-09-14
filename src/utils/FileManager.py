import json
from models.SceneData import SceneData

class FileManager:

    @staticmethod
    def load_scenes_from_json(path: str):
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        scenes = {}
        for scene in data["scenes"]:
            scenes[scene["id"]] = SceneData(
                scene_id=scene["id"],
                text=scene["text"],
                audio=scene["audio"],
                options=scene["options"]
            )
        return scenes
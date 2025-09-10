from openal import oalOpen, oalQuit

class SoundManager:
    def __init__(self):
        self.sounds = {}

    def load_sound(self, name, path):
        try:
            sound = oalOpen(path)
            if sound:
                self.sounds[name] = sound
            else:
                print(f"Error al cargar: {path}")
        except Exception as e:
            print(f"Error cargando {path}: {e}")

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()
        else:
            print(f"Sonido '{name}' no encontrado")
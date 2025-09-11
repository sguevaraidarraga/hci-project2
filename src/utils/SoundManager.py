import threading
import time
import os
from openal import oalInit, oalQuit, oalOpen

class SoundManager:
    def __init__(self):
        oalInit()
        self.sounds = {
            "intro": ("assets/sounds/ejemplo.wav", (0.0, 0.0, 0.0)),
            "fritura": ("assets/sounds/fritura.wav", (-1.0, 0.0, 0.0)),
            "techno": ("assets/sounds/techno.wav", (0.0, 0.0, -1.0)),
            "puerta": ("assets\sounds\Door Opening Sound Effect (1).wav", (0.5, 0.0, 0.0)),
            "mar": ("assets/sounds/mar.wav", (0.0, 0.0, -1.0)),
            "guardia": ("assets/sounds/guardia.wav", (1.0, 0.0, 0.0)),
            "dj_set": ("assets/sounds/dj_set.wav", (0.0, 1.0, 0.0)),
            "abbey_road": ("assets/sounds/ComeTogether.wav", (0.0, 0.0, 1.0)),
            "golpe": ("assets/sounds/golpe.wav", (-0.5, -0.5, 0.0)),
            "exito": ("assets/sounds/exito.wav", (0.0, 0.5, 0.0)),
            "ambiente": ("assets/sounds/ambiente.wav", (0.0, 0.0, 0.0)),
            "susurro": ("assets/sounds/revelacion.wav", (-0.8, 0.0, 0.0)),
            "misterio": ("assets/sounds/misterio.wav", (0.0, 0.0, -0.8)),
            "final_triunfo": ("assets/sounds/exito.wav", (0.0, 1.0, 0.0)),
            "eco": ("assets/sounds/eco.wav", (0.0, 0.0, -1.0)),
            "despertar": ("assets/sounds/despertar.wav", (0.0, 0.0, 1.0)),
            "revelacion": ("assets/sounds/revelacion.wav", (0.0, 0.0, 0.0)),
            "recorrido": ("assets/sounds/misterio.wav", (-0.5, 0.0, -0.5)),
            "vacio": ("assets/sounds/eco.wav", (0.0, -1.0, 0.0)),
        }
        self.loaded = {}
        self.moving = False
        self.thread = None
        self.current_source = None 

    def play(self, ref: str):
        self.stop_all()

        if ref not in self.sounds:
            print(f"[WARN] Sonido '{ref}' no definido en SoundManager")
            return

        path, position = self.sounds[ref]

        if not os.path.exists(path):
            print(f"[WARN] Archivo de sonido no encontrado: {path}")
            return

        if ref not in self.loaded:
            try:
                self.loaded[ref] = oalOpen(path)
            except Exception as e:
                print(f"[ERROR] No se pudo cargar '{path}': {e}")
                return

        source = self.loaded[ref]
        source.set_position(position)
        source.play()


        self.current_source = source

        if ref == "intro":
            if not self.moving:
                self.moving = True
                self.thread = threading.Thread(
                    target=self._move_intro_once, args=(source,), daemon=True
                )
                self.thread.start()

    def _move_intro_once(self, source):

        x = -1.0
        step = 0.05
        try:
            while self.moving and x <= 1.0:
                if not self.moving:
                    break
                try:
                    if source.get_state() != 4114:  # AL_PLAYING
                        break
                except Exception:
                    break
                source.set_position((x, 0.0, 0.0))
                x += step
                time.sleep(0.05) 
        except Exception as e:
            print("[ERROR hilo intro]", e)
        finally:
            self.moving = False

    def stop_all(self):

        self.moving = False

        if self.current_source:
            try:
                self.current_source.stop()
            except Exception:
                pass
            self.current_source = None

        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=0.2)

        for src in self.loaded.values():
            try:
                src.stop()
            except Exception:
                pass

    def __del__(self):
        try:
            self.stop_all()
            oalQuit()
        except Exception:
            pass

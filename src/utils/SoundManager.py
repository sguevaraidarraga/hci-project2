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
            "puerta": ("assets/sounds/Door Opening Sound Effect (1).wav", (0.5, 0.0, 0.0)),
            "mar": ("assets/sounds/mar.wav", (0.0, 0.0, -1.0)),
            "guardia": ("assets/sounds/guardia.wav", (1.0, 0.0, 0.0)),
            "dj_set": ("assets/sounds/dj_set.wav", (0.0, 1.0, 0.0)),
            "abbey_road": ("assets/sounds/ComeTogether.wav", (0.0, 0.0, 1.0)),
            "golpe": ("assets/sounds/golpe.wav", (-0.5, -0.5, 0.0)),
            "exito": ("assets/sounds/okay.wav", (0.0, 0.5, 0.0)),
            "ambiente": ("assets/sounds/ambiente.wav", (0.0, 0.0, 0.0)),
            "susurro": ("assets/sounds/revelacion.wav", (-0.8, 0.0, 0.0)),
            "misterio": ("assets/sounds/misterio.wav", (0.0, 0.0, -0.8)),
            "final_triunfo": ("assets/sounds/exito.wav", (0.0, 1.0, 0.0)),
            "eco": ("assets/sounds/eco.wav", (0.0, 0.0, -1.0)),
            "despertar": ("assets/sounds/despertar.wav", (0.0, 0.0, 1.0)),
            "revelacion": ("assets/sounds/revelacion.wav", (0.0, 0.0, 0.0)),
            "recorrido": ("assets/sounds/misterio.wav", (-0.5, 0.0, -0.5)),
            "vacio": ("assets/sounds/eco.wav", (0.0, -1.0, 0.0)),
            

            "intro_lejano": ("assets/sounds/ejemplo.wav", (0.0, 0.0, -2.0)),         
            "intro_muy_lejano": ("assets/sounds/ejemplo.wav", (0.0, 0.0, -4.0)),      
            "intro_artificial": ("assets/sounds/ejemplo.wav", (-2.0, -1.0, 0.0)),     
            "intro_distorsionado": ("assets/sounds/ejemplo.wav", (-3.0, -2.0, -1.0)), 
            "intro_memoria": ("assets/sounds/ejemplo.wav", (0.0, 2.0, 3.0)),          
            "intro_fantasma": ("assets/sounds/ejemplo.wav", (-4.0, 0.0, -4.0)),       
            

            "techno_amortiguado": ("assets/sounds/techno.wav", (0.0, -1.0, -2.0)),    
            "techno_distante": ("assets/sounds/techno.wav", (2.0, 0.0, -3.0)),        
            "techno_eco": ("assets/sounds/techno.wav", (1.0, 1.0, -2.0)),             
            "techno_creciente": ("assets/sounds/techno.wav", (0.0, 0.0, -0.5)),       
            "techno_susurrado": ("assets/sounds/techno.wav", (-2.0, 0.0, -2.0)),      
            "techno_revelacion": ("assets/sounds/techno.wav", (0.0, 0.5, -1.0)),      
            "techno_dimensional": ("assets/sounds/techno.wav", (3.0, 2.0, -5.0)),    
            "techno_memoria": ("assets/sounds/techno.wav", (1.0, 3.0, 2.0)),          
            "techno_transformacion": ("assets/sounds/techno.wav", (0.0, 0.0, -1.5)),  
            "techno_alma": ("assets/sounds/techno.wav", (0.0, 1.5, 0.0)),             
            "techno_fantasma": ("assets/sounds/techno.wav", (-5.0, 1.0, -3.0)),       
            

            "ambiente_underground": ("assets/sounds/ambiente.wav", (0.0, -2.0, 0.0)), 
            "ambiente_multitud": ("assets/sounds/ambiente.wav", (0.0, 0.0, 0.5)),     
            "ambiente_moribundo": ("assets/sounds/ambiente.wav", (0.0, -3.0, -2.0)), 
            

            "fritura_eco": ("assets/sounds/fritura.wav", (-1.5, 0.0, -1.0)),          
            "fritura_baja": ("assets/sounds/fritura.wav", (-1.0, -0.5, 0.0)),         
            

            "mar_triunfante": ("assets/sounds/mar.wav", (0.0, 2.0, -1.0)),          
            "mar_guia": ("assets/sounds/mar.wav", (0.5, 0.0, -1.5)),                  
            

            "dj_set_climax": ("assets/sounds/dj_set.wav", (0.0, 3.0, 0.0)),           
            "dj_set_emocional": ("assets/sounds/dj_set.wav", (0.0, 1.5, 0.5)),        
            

            "abbey_road_eco": ("assets/sounds/ComeTogether.wav", (2.0, 0.0, 2.0)),    
            

            "revelacion_final": ("assets/sounds/revelacion.wav", (0.0, 2.0, 0.0)),    
            "revelacion_profunda": ("assets/sounds/revelacion.wav", (0.0, 0.0, 0.5)), 
            

            "misterio_lejano": ("assets/sounds/misterio.wav", (3.0, 0.0, -2.0)),     
            "misterio_final": ("assets/sounds/misterio.wav", (0.0, 1.0, 1.0)),       

            "eco_eterno": ("assets/sounds/eco.wav", (0.0, 4.0, -6.0)),               
        }
        
        self.loaded = {}
        self.moving = False
        self.thread = None
        self.current_sources = []

    def play(self, ref):
        self.stop_all()


        if isinstance(ref, str):
            refs = [ref]
        elif isinstance(ref, list):
            refs = ref
        else:
            print(f"[WARN] Audio reference must be string or list, got {type(ref)}")
            return


        for sound_ref in refs:
            self._play_single(sound_ref)

    def _play_single(self, ref: str):
        if ref not in self.sounds:
            print(f"[WARN] Sound '{ref}' not defined")
            return

        path, position = self.sounds[ref]

        if not os.path.exists(path):
            print(f"[WARN] File Not Found: {path}")
            return

        if ref not in self.loaded:
            try:
                self.loaded[ref] = oalOpen(path)
            except Exception as e:
                print(f"[ERROR] Error Loading '{path}': {e}")
                return

        source = self.loaded[ref]
        source.set_position(position)
        source.play()

        self.current_sources.append(source)


        if "intro" in ref:
            if not self.moving:
                self.moving = True
                self.thread = threading.Thread(
                    target=self._move_intro_once, args=(source,), daemon=True
                )
                self.thread.start()

    def _move_intro_once(self, source):
        position_x = -1.0         
        step_size = 0.05           
        update_interval = 0.05     

        try:
            while self.moving and position_x <= 1.0:
                if not self.moving:
                    break

                try:
                    if source.get_state() != 4114:  
                        break
                except Exception:
                    break

                source.set_position((position_x, 0.0, 0.0))
                position_x += step_size
                time.sleep(update_interval)

        except Exception as error:
            print("[ERROR intro thread]", error)

        finally:
            self.moving = False

    def stop_all(self):
        self.moving = False

        for source in self.current_sources:
            try:
                source.stop()
            except Exception:
                pass
        
        self.current_sources.clear()

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

# Azul Macadamia

[Video](https://javerianacaliedu-my.sharepoint.com/:v:/g/personal/juango26_javerianacali_edu_co/EelpXWVrH5FIvvOlJmOUDXABisvxpMVpnZb9zjWHMO-qYQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=TS3btm)

## Authors
- Juan David Vasquez Pomar
- Santiago Guevara Idarraga

---

## Project Description
**Azul Macadamia** is a **text-based interactive adventure game** inspired by Zork.
The narrative is accompanied by **diegetic and spatialized sounds**, using **OpenAL** for 3D audio rendering.
The objective is to create an **immersive auditory world** where the player advances through the story by reading line by line and making decisions.

- The story lasts at least **5 minutes**.
- It includes more than **50 lines of text** with a complete structure: introduction, development, climax, and ending.
- Every line of the story is paired with a **sound effect or piece of music** placed in the 3D space (left, right, behind, distant, etc.).
- The user interacts through a **command-line interface (CLI)**.
- The project is implemented in **Python** following **Object-Oriented Programming (OOP)** principles.

---

## Technical Design

### Structure
- **`src/models/`**: Data classes (`SceneData`) representing story elements.
- **`src/utils/`**: Loaders for external resources (JSON → Python objects).
- **`src/managers/`**: Game logic (scene management, user choices).
- **`assets/`**: Contains all non-code resources:
  - `ascii/` → ASCII art
  - `sounds/` → Audio files
  - `scripts/` → Narrative files (`scenes.json`)

### Workflow
1. The **story** is stored in JSON format with scenes, text, audio references, and options.
2. The **FileManager** reads the JSON and builds the scene graph.
3. The **SceneManager** runs the game loop:
   - Displays the text line by line.
   - Plays spatialized audio using OpenAL.
   - Presents choices to the player.
   - Navigates through the graph according to user input.

---

## Why This Approach?
We chose this modular, JSON-driven architecture because:
- **Scalability**: The narrative can be modified or extended without touching the code (just editing the JSON).
- **Flexibility**: Separation between *data* (story, sounds) and *logic* (scene manager) improves maintainability.
- **Reusability**: The engine can be reused for different stories simply by replacing the JSON script and audio files.
- **Clean Code**: Following OOP principles makes the project organized and easier to test.

---

## Requirements
- Python 3.10+
- OpenAL library (for 3D sound support)
- Recommended: Virtual environment for dependencies

---

## How to Run
```bash
# Create and activate virtual environment
python -m venv venv

# Activate virtual enviroment
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run the game
python src/main.py
```

## License

This project was developed for academic purposes in the course Sistemas de Interacción.
All sounds and music used are for educational use only.

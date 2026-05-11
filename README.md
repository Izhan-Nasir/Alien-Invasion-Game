# 👾 Alien Invasion

A classic arcade-style space shooter built with Python and Pygame. Defend Earth by destroying waves of aliens before they reach the bottom of the screen — each level gets faster, harder, and worth more points.

---

## Gameplay

- **Move** your ship left and right using the arrow keys
- **Shoot** bullets with the spacebar
- Destroy all aliens to advance to the next level
- You have **3 lives** — lose one every time an alien reaches your ship or the bottom of the screen
- The game ends when all lives are lost

## Features

- 🚀 Progressively increasing difficulty — alien speed and bullet size scale with each level
- 🏆 Persistent high score saved locally to `Highscore.json`
- 📊 On-screen HUD showing current score, high score, level, and remaining lives
- 🎵 Dynamic music playlist that cycles through tracks during gameplay, with a separate menu theme
- 🔊 Sound effects for shooting, alien kills, level-ups, and losing a life

## Controls

| Key         | Action          |
|-------------|-----------------|
| `←` / `→`  | Move ship       |
| `Space`     | Fire bullet     |
| `Q`         | Quit game       |

## Installation

**Requirements:** Python 3.x

1. Clone the repository:
```bash
   git clone https://github.com/your-username/Alien-Invasion-Game.git
   cd Alien-Invasion-Game
```

2. Create and activate a virtual environment (VS Code recommended):
```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
```

3. Install dependencies:
```bash
   pip install -r Requirements.txt
```

4. Run the game:
```bash
   python alien_invasion.py
```

## Project Structure

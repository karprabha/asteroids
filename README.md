# Asteroids Game 🚀

A classic Asteroids arcade game implementation built with Python and Pygame. Navigate through space, shoot asteroids, and try to survive as long as possible!

## 🎮 Game Overview

This is a faithful recreation of the classic Asteroids arcade game where you pilot a spaceship through an asteroid field. Your goal is to destroy asteroids while avoiding collisions. When you shoot large asteroids, they split into smaller ones, creating an increasingly challenging environment.

## ✨ Features

- **Classic Asteroids Gameplay**: Authentic recreation of the arcade classic
- **Smooth Controls**: Responsive keyboard controls for movement and shooting
- **Asteroid Physics**: Asteroids split into smaller pieces when shot
- **Collision Detection**: Precise collision detection between player, asteroids, and shots
- **Continuous Asteroid Spawning**: New asteroids continuously appear to maintain challenge
- **60 FPS Gameplay**: Smooth 60 frames per second gameplay

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/karprabha/asteroids.git
   cd asteroids
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   uv pip install -r requirements.txt
   ```

4. **Run the game**:
   ```bash
   uv run main.py
   ```

## 🎯 How to Play

### Controls

- **W** - Move forward (thrust)
- **S** - Move backward
- **A** - Rotate left
- **D** - Rotate right
- **SPACEBAR** - Shoot

### Gameplay

1. Use **W/S** to move your triangular spaceship forward and backward
2. Use **A/D** to rotate your ship left and right
3. Press **SPACEBAR** to shoot projectiles at asteroids
4. Avoid colliding with asteroids - collision ends the game
5. When you shoot an asteroid, it splits into two smaller asteroids
6. Smaller asteroids are destroyed completely when shot
7. New asteroids continuously spawn to keep the challenge going

## 🏗️ Project Structure

```
asteroids/
├── main.py          # Main game loop and initialization
├── player.py        # Player ship class and controls
├── asteroid.py      # Asteroid class and behavior
├── asteroidfield.py # Asteroid spawning system
├── shot.py          # Projectile class
├── circleshape.py   # Base class for circular game objects
├── constants.py     # Game configuration and constants
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## 🔧 Configuration

Game settings can be modified in `constants.py`:

- **Screen dimensions**: 1280x720 pixels
- **Player settings**: Speed, turn rate, shoot cooldown
- **Asteroid settings**: Size, spawn rate, minimum radius
- **Shot settings**: Speed and size

## 🎨 Technical Details

- **Engine**: Pygame 2.6.1
- **Language**: Python 3
- **Architecture**: Object-oriented design with sprite groups
- **Physics**: Simple 2D vector-based movement
- **Rendering**: 60 FPS with double buffering

## 🚧 Game Architecture

The game follows a clean object-oriented design:

- **CircleShape**: Base class for all circular game objects
- **Player**: Handles spaceship movement, rotation, and shooting
- **Asteroid**: Manages asteroid behavior and splitting mechanics
- **AsteroidField**: Spawns new asteroids at regular intervals
- **Shot**: Handles projectile physics and lifecycle

## 🎯 Future Enhancements

Potential improvements and features:

- [ ] Score system
- [ ] Lives/health system
- [ ] Power-ups
- [ ] Sound effects and background music
- [ ] Different asteroid types
- [ ] Particle effects
- [ ] High score tracking
- [ ] Game over screen with restart option
- [ ] Difficulty levels

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by the classic Asteroids arcade game by Atari (1979)
- Built with [Pygame](https://www.pygame.org/) - thanks to the Pygame community
- Special thanks to the retro gaming community for keeping classics alive

---

**Enjoy the game! 🚀 Try to survive as long as possible in the asteroid field!**

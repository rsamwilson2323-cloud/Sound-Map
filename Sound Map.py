# ================== SILENCE WARNINGS ==================
import warnings
warnings.filterwarnings("ignore")

# ================== IMPORTS ==================
import sounddevice as sd
import numpy as np
import pygame
import threading
import time
import sys

# ================== CONFIG ==================
WIDTH, HEIGHT = 800, 500
GRID = 25
FPS = 60
RATE = 16000
BLOCK = 256

NOISE_FLOOR = 0.005   # detects tiny sounds
GAIN = 22.0           # amplifies quiet input
SMOOTHING = 0.80      # stable but responsive
DECAY = 0.975         # smooth fade
# ============================================

sound_level = 0.0
running = True

# ================== AUDIO CALLBACK ==================
def audio_callback(indata, frames, time_info, status):
    global sound_level

    raw = np.mean(np.abs(indata))

    # remove background noise floor
    level = max(0.0, raw - NOISE_FLOOR)

    # amplify small sounds
    level = min(level * GAIN, 1.0)

    # smooth but responsive
    sound_level = (sound_level * SMOOTHING) + (level * (1 - SMOOTHING))

# ================== AUDIO THREAD ==================
def audio_thread():
    with sd.InputStream(
        channels=1,
        samplerate=RATE,
        blocksize=BLOCK,
        callback=audio_callback
    ):
        while running:
            time.sleep(0.01)

# ================== PYGAME INIT ==================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎧 Sound Map of Your Room")
clock = pygame.time.Clock()

cols = WIDTH // GRID
rows = HEIGHT // GRID
terrain = np.zeros((cols, rows))

# ================== START AUDIO ==================
threading.Thread(target=audio_thread, daemon=True).start()

print("🎧 Listening to room sound...")
print("🗺️ Visualizing sound as terrain")
print("➡️ Press ENTER to exit")

# ================== MAIN LOOP ==================
while running:
    clock.tick(FPS)

    # ignore all events
    pygame.event.pump()

    # ONLY ENTER exits
    if pygame.key.get_pressed()[pygame.K_RETURN]:
        running = False

    # motion
    terrain = np.roll(terrain, 1, axis=0)

    # inject sound
    terrain[0, :] = sound_level

    # decay
    terrain *= DECAY

    # draw
    screen.fill((8, 8, 12))

    for x in range(cols):
        for y in range(rows):
            v = terrain[x, y]

            r = int(60 + v * 195)
            g = int(50 + v * 135)
            b = int(130 + v * 125)

            pygame.draw.rect(
                screen,
                (r, g, b),
                (x * GRID, y * GRID, GRID - 2, GRID - 2)
            )

    pygame.display.flip()

# ================== CLEAN EXIT ==================
pygame.quit()
sys.exit()

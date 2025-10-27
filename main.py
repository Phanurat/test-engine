import pygame
import math

# =========================
#   ตั้งค่าเริ่มต้นเกม
# =========================
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini MMORPG Engine - Example")

clock = pygame.time.Clock()
FPS = 60

# =========================
#   โหลด Background
# =========================
background = pygame.image.load("assets/bg/bg.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# =========================
#   โหลด Sprite ของ Player
# =========================
player_sprites = {
    "back": pygame.image.load("assets/player/Back.png"),
    "down": pygame.image.load("assets/player/Down.png"),
    "sit": pygame.image.load("assets/player/Sit.png"),
    "up": pygame.image.load("assets/player/Up.png"),
    "walk": pygame.image.load("assets/player/Walk.png")
}

# ปรับขนาดทั้งหมดให้เท่ากัน (ถ้าใหญ่เกินไป)
for key in player_sprites:
    player_sprites[key] = pygame.transform.scale(player_sprites[key], (64, 64))

# =========================
#   คลาส Player
# =========================
class Player:
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.sprites = sprites
        self.current = "down"
        self.speed = 3
        self.target = None

    def move_to(self, target):
        self.target = target

    def update(self):
        if self.target:
            dx = self.target[0] - self.x
            dy = self.target[1] - self.y
            dist = math.hypot(dx, dy)

            if dist < self.speed:
                self.target = None
                self.current = "sit"  # หยุดนั่ง
            else:
                # เดินไปยังเป้าหมาย
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist

                # เปลี่ยนทิศทาง
                if abs(dx) > abs(dy):
                    self.current = "back" if dx < 0 else "down"
                else:
                    self.current = "up" if dy < 0 else "down"
        else:
            # ถ้าไม่ได้เดินเลย ให้ท่า default = down
            if self.current != "sit":
                self.current = "down"

    def draw(self, surface):
        sprite = self.sprites[self.current]
        surface.blit(sprite, (self.x, self.y))

# =========================
#   สร้าง Player
# =========================
player = Player(100, 100, player_sprites)

# =========================
#   ลูปหลักของเกม
# =========================
running = True
while running:
    # ---- Input Event ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # คลิกซ้ายเพื่อเดิน
                player.move_to(event.pos)

    # ---- Update Logic ----
    player.update()

    # ---- Draw Everything ----
    screen.blit(background, (0, 0))  # วาดฉากหลัง
    player.draw(screen)              # วาดผู้เล่น
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

import pygame
import math

# ======================================
# 🔧 ตั้งค่าเริ่มต้นของเกม
# ======================================
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini MMORPG Engine - Highlighted Player")

clock = pygame.time.Clock()
FPS = 60

# ======================================
# 🌄 โหลด Background
# ======================================
background = pygame.image.load("assets/bg/bg.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# ======================================
# 🧍 โหลด Sprite ของ Player
# ======================================
player_sprites = {
    "back": pygame.image.load("assets/player/Back.png"),
    "down": pygame.image.load("assets/player/Down.png"),
    "idle": pygame.image.load("assets/player/Sit.png"),  # ใช้ Sit.png เป็นท่ายืน
    "up": pygame.image.load("assets/player/Up.png"),
    "walk": pygame.image.load("assets/player/Walk.png"),
}

# ปรับขนาดทุก sprite ให้เท่ากัน
for key in player_sprites:
    player_sprites[key] = pygame.transform.scale(player_sprites[key], (64, 64))

# ======================================
# 🧠 คลาส Player
# ======================================
class Player:
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.sprites = sprites
        self.current = "idle"
        self.speed = 3
        self.target = None
        self.selected = True  # แสดงวงแหวนรอบตัว

    def move_to(self, target):
        self.target = target

    def update(self):
        if self.target:
            dx = self.target[0] - self.x
            dy = self.target[1] - self.y
            dist = math.hypot(dx, dy)

            if dist < self.speed:
                self.target = None
                self.current = "idle"
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
            self.current = "idle"

    def draw(self, surface):
        sprite = self.sprites[self.current]

        # ===== วาดเงาใต้เท้า =====
        shadow = pygame.Surface((50, 20), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow, (0, 0, 0, 100), shadow.get_rect())
        surface.blit(shadow, (self.x + 7, self.y + 48))

        # ===== วาดวงแหวนเรืองแสงรอบเท้า =====
        if self.selected:
            glow = pygame.Surface((70, 30), pygame.SRCALPHA)
            pygame.draw.ellipse(glow, (0, 255, 0, 80), glow.get_rect())
            surface.blit(glow, (self.x - 5, self.y + 40))

        # ===== วาด Outline รอบตัวละคร =====
        outline = sprite.copy()
        outline.fill((0, 0, 0), special_flags=pygame.BLEND_RGB_MULT)
        for ox, oy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            surface.blit(outline, (self.x + ox, self.y + oy))

        # ===== วาดตัวละครจริง =====
        surface.blit(sprite, (self.x, self.y))

# ======================================
# 🧍 สร้าง Player
# ======================================
player = Player(100, 100, player_sprites)

# ======================================
# 🎮 ลูปหลักของเกม
# ======================================
running = True
while running:
    # ----- Input -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # คลิกซ้ายเพื่อสั่งเดิน
                player.move_to(event.pos)

    # ----- Update -----
    player.update()

    # ----- Draw -----
    screen.blit(background, (0, 0))  # พื้นหลัง
    player.draw(screen)              # วาดผู้เล่น
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

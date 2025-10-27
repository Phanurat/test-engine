import pygame

# Initialize pygame
pygame.init()

# ตั้งค่าขนาดหน้าต่าง
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My RTS Engine")

# ตั้งค่า FPS
clock = pygame.time.Clock()
FPS = 60

# Game loop
running = True
while running:
    # 1. Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update game state
    # (เรายังไม่มีวัตถุอะไรตอนนี้)

    # 3. Render
    screen.fill((50, 50, 50))  # สีพื้นหลัง
    pygame.display.flip()

    # ควบคุม FPS
    clock.tick(FPS)

pygame.quit()

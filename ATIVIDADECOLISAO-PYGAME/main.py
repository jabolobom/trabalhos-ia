import pygame
import sys

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("TESTE SPRITE")

white = (255,255,255)
gray = (200,200,200)
black = (0,0,0)

sprite_sheet = pygame.image.load("Attack.png").convert_alpha()
frame_n = 8

frame_width = sprite_sheet.get_width() // frame_n # divide em 8 partes a largura total
frame_height = sprite_sheet.get_height()

frames = [sprite_sheet.subsurface((i * frame_width, 52, frame_width, frame_height - 52)) for i in range(frame_n)]  

def draw_bt(screen, color, pos, size, text):
    fontfamily = pygame.font.Font(None, 36)
    pygame.draw.rect(screen, color, (pos[0],pos[1], size[0], size[1]))
    surface_text = fontfamily.render(text, True, black)
    # meio da tela
    text_rect = surface_text.get_rect(center=(pos[0] + size[0] // 2, pos[1] + size[1] // 2)) 
    screen.blit(surface_text, text_rect)


btn_width, btn_height = 100, 50
x_btn = width - btn_width - 10
y_btn = height - btn_height - 10

frame_index = 0
frame_time = 200#ms
timer = 0
last_time = pygame.time.get_ticks()

pos_x = 10
pos_y = 10
movement = 1

running = True
while running:
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            running = False
        elif x.type == pygame.MOUSEBUTTONDOWN:
            if btn.collidepoint(x.pos): # se o clique for em cima da collide area do botao
                running = False # breika


    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        pos_x += movement
    if keys[pygame.K_LEFT]:
        pos_x -= movement
    if keys[pygame.K_DOWN]:
        pos_y += movement
    if keys[pygame.K_UP]:
        pos_y -= movement

    # retangulo de colisao
    sprite_collision = pygame.Rect(pos_x,pos_y, frame_width, frame_height - 52)
    # limitando o espaço do sprite
    pos_x = max(0, min(pos_x, width - frame_width))
    pos_y = max(0, min(pos_y, height - (frame_height - 52)))

    nowT = pygame.time.get_ticks()
    if nowT - last_time > frame_time:
        frame_index = (frame_index + 1) % frame_n
        last_time = nowT


    screen.fill(white)
    screen.blit(frames[frame_index], (pos_x, pos_y))

    btn = pygame.Rect(x_btn // 2, y_btn // 2, btn_width, btn_height ) # botando no meio
    draw_bt(screen, gray, btn.topleft, btn.size, "EXITAR")

    # !!!!
    if sprite_collision.colliderect(btn):
        if keys[pygame.K_RIGHT]:
            pos_x -= movement
        if keys[pygame.K_LEFT]:
            pos_x += movement
        if keys[pygame.K_DOWN]:
            pos_y -= movement
        if keys[pygame.K_UP]:
            pos_y += movement
    # COLISAO, EMPURRA O SPRITE PRO LADO CONTRÁRIO QUANDO COLIDE

    pygame.display.flip()

pygame.quit()
sys.exit()
    


import pygame
import sys
pygame.init()
AN, AL = 800, 600
P=pygame.display.set_mode((AN,AL))
pygame.display.set_caption("Mover el cuadrado")
clock=pygame.time.Clock()
C=pygame.Rect(100,100,50,50)
V=5
while True:
    for E in pygame.event.get():
        if E.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    T=pygame.key.get_pressed()
    if T[pygame.K_w] or T[pygame.K_UP]:
        if C.top>0:
            C.y-=V
    if T[pygame.K_s] or T[pygame.K_DOWN]:
        if C.bottom < AL:
            C.y+=V
    if T[pygame.K_a] or T[pygame.K_LEFT]:
        if C.left > 0:
            C.x-=V
    if T[pygame.K_d] or T[pygame.K_RIGHT]:
        if C.right < AN:
            C.x+=V
    P.fill((30,30,30))
    pygame.draw.rect(P,(0,255,0),C)
    pygame.display.flip()
    clock.tick(60)
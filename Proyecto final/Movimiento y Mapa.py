import pygame
import sys

pygame.init()
AN, AL = 800, 600  # Tamaño de la ventana
P = pygame.display.set_mode((AN, AL))
pygame.display.set_caption("Cámara sigue al jugador")

clock = pygame.time.Clock()
C = pygame.Rect(1600, 1200, 50, 50)  # Jugador empieza en el centro del mapa
V = 5

# Cargar imagen del mapa (fondo)
fondo = pygame.image.load("pixel_image_proportional_3200x2400.png").convert()
mapa_ancho, mapa_alto = fondo.get_size()

while True:
    for E in pygame.event.get():
        if E.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    T = pygame.key.get_pressed()
    if T[pygame.K_w] or T[pygame.K_UP]:
        C.y -= V
    if T[pygame.K_s] or T[pygame.K_DOWN]:
        C.y += V
    if T[pygame.K_a] or T[pygame.K_LEFT]:
        C.x -= V
    if T[pygame.K_d] or T[pygame.K_RIGHT]:
        C.x += V

    # Limitar al área del mapa
    C.x = max(0, min(C.x, mapa_ancho - C.width))
    C.y = max(0, min(C.y, mapa_alto - C.height))

    # Calcular desplazamiento de cámara
    cam_x = C.x - AN // 2 + C.width // 2
    cam_y = C.y - AL // 2 + C.height // 2

    # Limitar cámara al borde del mapa
    cam_x = max(0, min(cam_x, mapa_ancho - AN))
    cam_y = max(0, min(cam_y, mapa_alto - AL))

    # Dibujar fondo (mapa desplazado)
    P.blit(fondo, (-cam_x, -cam_y))

    # Dibujar jugador centrado en pantalla
    jugador_pantalla = pygame.Rect(C.x - cam_x, C.y - cam_y, C.width, C.height)
    pygame.draw.rect(P, (128, 0, 128), jugador_pantalla)

    pygame.display.flip()
    clock.tick(60)

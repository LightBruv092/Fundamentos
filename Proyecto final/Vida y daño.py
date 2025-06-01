import pygame
import sys
import math

pygame.init()
AN, AL = 800, 600
P = pygame.display.set_mode((AN, AL))
pygame.display.set_caption("Pantalla de inicio")
clock = pygame.time.Clock()

# Estado del juego
estado = "menu"

# Botón
boton_rect = pygame.Rect(AN // 2 - 100, AL // 2 - 25, 200, 50)
fuente = pygame.font.SysFont(None, 40)

# Fondo y jugador (cargados solo si se entra al juego)
fondo = pygame.image.load("pixel_image_proportional_3200x2400.png").convert()
mapa_ancho, mapa_alto = fondo.get_size()
cuadro_ancho, cuadro_alto = 50, 50
C = pygame.Rect(
    mapa_ancho // 2 - cuadro_ancho // 2,
    mapa_alto // 2 - cuadro_alto // 2,
    cuadro_ancho,
    cuadro_alto
)
V = 5
V_base = 5
V_ralentizado = 2

# Vida
vida = 100
vida_max = 100
tiempo_ultimo_daño = pygame.time.get_ticks()
intervalo_daño = 2000  # 2 segundos

# ==== ENEMIGOS ====
ENEMIGOS = []
VELOCIDAD_ENEMIGO = 2
ULTIMA_CREACION = pygame.time.get_ticks()
INTERVALO_CREACION = 6000  # milisegundos

def crear_enemigo():
    x, y = 100, 100
    enemigo = pygame.Rect(x, y, cuadro_ancho, cuadro_alto)
    ENEMIGOS.append(enemigo)

def mover_hacia_jugador(enemigo):
    dx = C.centerx - enemigo.centerx
    dy = C.centery - enemigo.centery
    distancia = math.hypot(dx, dy)
    if distancia != 0:
        dx /= distancia
        dy /= distancia
        enemigo.x += int(dx * VELOCIDAD_ENEMIGO)
        enemigo.y += int(dy * VELOCIDAD_ENEMIGO)

def evitar_superposicion():
    for i in range(len(ENEMIGOS)):
        for j in range(i + 1, len(ENEMIGOS)):
            e1, e2 = ENEMIGOS[i], ENEMIGOS[j]
            if e1.colliderect(e2):
                dx = e1.centerx - e2.centerx
                dy = e1.centery - e2.centery
                distancia = math.hypot(dx, dy) or 1
                separacion = 5
                moverx = (dx / distancia) * separacion
                movery = (dy / distancia) * separacion
                e1.x += int(moverx)
                e1.y += int(movery)
                e2.x -= int(moverx)
                e2.y -= int(movery)

def dibujar_barra_vida(surface, x, y, ancho, alto, vida, vida_max):
    pygame.draw.rect(surface, (255, 0, 0), (x, y, ancho, alto))  # fondo rojo
    ancho_vida = int((vida / vida_max) * ancho)
    pygame.draw.rect(surface, (0, 255, 0), (x, y, ancho_vida, alto))  # barra verde

# Bucle principal
while True:
    for E in pygame.event.get():
        if E.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif E.type == pygame.MOUSEBUTTONDOWN and estado == "menu":
            if boton_rect.collidepoint(E.pos):
                estado = "jugando"

    if estado == "menu":
        P.fill((20, 20, 20))

        # Botón "Jugar"
        pygame.draw.rect(P, (0, 100, 200), boton_rect)
        texto_jugar = fuente.render("Jugar", True, (255, 255, 255))
        texto_jugar_rect = texto_jugar.get_rect(center=boton_rect.center)
        P.blit(texto_jugar, texto_jugar_rect)

        # Botón "Salir"
        boton_salir_rect = pygame.Rect(AN // 2 - 100, AL // 2 + 50, 200, 50)
        pygame.draw.rect(P, (200, 0, 0), boton_salir_rect)
        texto_salir = fuente.render("Salir", True, (255, 255, 255))
        texto_salir_rect = texto_salir.get_rect(center=boton_salir_rect.center)
        P.blit(texto_salir, texto_salir_rect)

        if pygame.mouse.get_pressed()[0]:  # Botón izquierdo
            mouse_pos = pygame.mouse.get_pos()
            if boton_salir_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    elif estado == "jugando":
        # Contar enemigos colisionando con el jugador
        enemigos_colisionando = sum(1 for enemigo in ENEMIGOS if C.colliderect(enemigo))
        ralentizado = enemigos_colisionando > 0

        # Velocidad según si hay contacto
        V = V_ralentizado if ralentizado else V_base

        # Aplicar daño según cuántos enemigos tocan al jugador
        tiempo_actual = pygame.time.get_ticks()
        if enemigos_colisionando > 0 and tiempo_actual - tiempo_ultimo_daño >= intervalo_daño:
            daño = 5 * enemigos_colisionando
            vida = max(0, vida - daño)
            tiempo_ultimo_daño = tiempo_actual

        # Movimiento
        T = pygame.key.get_pressed()
        if T[pygame.K_w] or T[pygame.K_UP]:
            C.y -= V
        if T[pygame.K_s] or T[pygame.K_DOWN]:
            C.y += V
        if T[pygame.K_a] or T[pygame.K_LEFT]:
            C.x -= V
        if T[pygame.K_d] or T[pygame.K_RIGHT]:
            C.x += V
        if T[pygame.K_ESCAPE]:
            estado = "menu"

        # Límites del mapa
        C.x = max(0, min(C.x, mapa_ancho - C.width))
        C.y = max(0, min(C.y, mapa_alto - C.height))

        # Cámara
        cam_x = C.x - AN // 2 + C.width // 2
        cam_y = C.y - AL // 2 + C.height // 2
        cam_x = max(0, min(cam_x, mapa_ancho - AN))
        cam_y = max(0, min(cam_y, mapa_alto - AL))

        # Dibujar fondo y jugador
        P.blit(fondo, (-cam_x, -cam_y))
        jugador_pantalla = pygame.Rect(C.x - cam_x, C.y - cam_y, C.width, C.height)
        pygame.draw.rect(P, (128, 0, 128), jugador_pantalla)

        # Dibujar barra de vida
        dibujar_barra_vida(P, 20, 20, 200, 20, vida, vida_max)

        # Enemigos: creación y movimiento
        if tiempo_actual - ULTIMA_CREACION >= INTERVALO_CREACION:
            crear_enemigo()
            ULTIMA_CREACION = tiempo_actual

        for enemigo in ENEMIGOS:
            mover_hacia_jugador(enemigo)

        evitar_superposicion()

        for enemigo in ENEMIGOS:
            enemigo_pantalla = pygame.Rect(
                enemigo.x - cam_x, enemigo.y - cam_y, enemigo.width, enemigo.height)
            pygame.draw.rect(P, (255, 0, 0), enemigo_pantalla)

    pygame.display.flip()
    clock.tick(60)

"""
Proyecto Snake Game python
El programa simula lo que es el juego de la serpiente de los antiguos teléfonos.
El programa usa la interfaz gráfica de pygame para renderizar el cuerpo de la serpiente y la manzana,
para moverse hay que usar las flechas.
"""

#librerías necesarias
import pygame, time, replit,random, sys

"""
Esta función inicializa los módulos importados de pygame
"""
pygame.init()


"""
================== funciones del juego  =====================================
"""

def posicion_fruta():
    """
    (uso de funciones, uso de operadores, uso de lisas)
    genera una lista de dos valores 
    devuelve: una coordenada aleatoria en x,y
    """
    posicion_random = random.randint (0,49)*10
    pos_fruta = [posicion_random, posicion_random]
    return pos_fruta

def puntuacion(score):
    """
    (Uso de fuciones, uso de operadores)
    recibe; score (valor numérico)
    Lo usa como un acumulador y le va sumano 1 
    cada vez que la serpiente se coma una manzana
    devuelve: la puntación del usuario
    """
    score += 1
    return score

def principal(valores_vel, snake_coordinates, cuerpo, pos_fruta, cambio, run, score):
    """
    (Uso de operadores, funciones, listas, matrices, ciclos, ciclos anidados, condicionales, condicionales anidados, boleanos)
    recibe: valores_vel (matriz de valores numéricos), snake_coordinates (lista de valores numéricos), 
    pos_fruta (variable que manda a llamar una función), cambio (Valor de tipo cadena), run (Valor de tipo boleano) y 
    score (valor numérico)
    Define el funcionamiento del juego y movimiento de la serpiente, así como también renderiza en pantalla la puntuación 
    del usuario y a la serpiente
    Al perder: manda a llamar la función para reegresar al menú, y entra a la función como parámetro 
    la puntuación previa obtenida
    """

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    cambio = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    cambio = "LEFT"
                elif event.key == pygame.K_UP:
                    cambio = "UP"
                elif event.key == pygame.K_DOWN:
                    cambio = "DOWN"
                    
        if cambio == "RIGHT":
            snake_coordinates[0] += 10
        elif cambio == "LEFT":
            snake_coordinates[0] -= 10
        elif cambio == "UP":
            snake_coordinates[1] -= 10
        elif cambio == "DOWN":
            snake_coordinates[1] += 10

        cuerpo.insert(0, list(snake_coordinates))

        if score < 5:
            fps.tick(valores_vel[0][0])
        elif score >=5 and score<10:
            fps.tick(valores_vel[0][1])
        elif score >= 10 and score < 15:
            fps.tick(valores_vel[1][0])
        elif score >= 15 and score < 20:
            fps.tick(valores_vel[1][1])

        if snake_coordinates == pos_fruta:
            pos_fruta = posicion_fruta()
            score = puntuacion(score)
        else:
            cuerpo.pop()

        cabeza = cuerpo[-1]
        for i in range(len(cuerpo) - 1):
            part = cuerpo[i]
            if cabeza[0] == part[0] and cabeza[1] == part[1]:
                run = False
                print("PERDISTE")
                menu(superficie_juego, text, instru, instru2, instru3)
                
        superficie_juego.fill((0,0,0))

        for pos in cuerpo:
            pygame.draw.rect(superficie_juego,(255,0,0), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(superficie_juego,(255,0,0), pygame.Rect(pos_fruta[0], pos_fruta[1], 10, 10))

        text = font.render(str(score),0,PERRY)
        superficie_juego.blit(text, (480,20))

        if snake_coordinates[0] <= 0 or snake_coordinates[0] >= 500:
            run = False
            print("PERDISTE")

            menu(superficie_juego, text, instru, instru2, instru3)  
        if snake_coordinates[1] <= 0 or snake_coordinates[1] >= 500:
            run = False
            print("PERDISTE")
            menu(superficie_juego, text, instru, instru2, instru3)
        
        pygame.display.flip()

def menu(superficie_juego, text, instru, instru2, instru3):
    """
    (Uso de fuciones, listas, condicionales, condicionales anidados, ciclos, ciclos anidados, boleanos)
    recibe: superficie_juego (funcion con una lista), text, instru, instru2, 
    instru3 (funciones de renderizado con listas de valores)
    Al terminar: manda a llamar la función principal para iniciar el juego
    """
    run2 = True
    background = BLACK


    while run2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run2 = False

        superficie_juego.fill(background)
        superficie_juego.blit(text, (120, 50))
        superficie_juego.blit(instru, (170, 200))    
        superficie_juego.blit(instru2, (100, 225))    
        superficie_juego.blit(instru3, (100, 400))  
        superficie_juego.blit(puntuacion_prev, (20, 20)) 
        pygame.display.update()

    principal(valores_vel,snake_coordinates, cuerpo, pos_fruta, cambio, run, score)

"""
========  parte principal del programa ========================================
"""

#Se definen variables esenciales para el color y para la velocidad de la serpiente
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
PERRY = (72, 201, 176)
WHITE = (244, 246, 247)

fps = pygame.time.Clock()

#Se definen las dimensiones de la ventana donde se renderiza el juego
superficie_juego = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake Game")

#Se definen las fuentes que se usarán para el texto renderizado
font = pygame.font.Font(None, 30)
font2 = pygame.font.SysFont(None, 30)

#Renderizado de las instrucciones y mensaje de bienvenida
text = font2.render("Bienvenido a Snake game", True, RED)
rect = text.get_rect()

instru = font2.render("Dentro del juego", True, RED)

instru2 = font2.render("Utiliza las flechas para moverte", True, RED)

instru3 = font2.render("Presiona espacio para empezar", True, WHITE)
rect = instru3.get_rect()
pygame.draw.rect(instru3, GRAY, rect, 1)

puntuacion_prev = font2.render("Puntuación previa:", True, PERRY)
rect = puntuacion_prev.get_rect()
pygame.draw.rect(puntuacion_prev, GRAY, rect, 1)

#Variables esenciales para el funcionamiento y coordenadas
valores_vel=[[15,20],[25,30]]
snake_coordinates =[200,100]
cuerpo = [[100,50],[90,50],[80,50]]
pos_fruta = posicion_fruta()
cambio = "RIGHT"
run = True
score = 0

menu(superficie_juego, text, instru, instru2, instru3)

pygame.quit()


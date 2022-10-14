#hay que correr "pip install pygame" y "pip install replit" en la consola para poder importar pygame, 
#librerías necesarias
import pygame, time, replit,random, sys

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
PERRY = (72, 201, 176)
WHITE = (244, 246, 247)
fps = pygame.time.Clock()

pygame.init()

superficie_juego = pygame.display.set_mode((500,500))
pygame.display.set_caption("Menú")

font2 = pygame.font.SysFont(None, 30)

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

font = pygame.font.Font(None, 30)

fps = pygame.time.Clock()


def posicion_fruta():

    posicion_random = random.randint (0,49)*10
    pos_fruta = [posicion_random, posicion_random]
    return pos_fruta

def puntuacion(score):
    score += 1
    return score

def loading(percent):
    for i in range(100):
        replit.clear()
        percent +=1
        print("""Snake game\nEstatus: cargando %"""+ str(percent)
            )
        time.sleep(.03)
  
    print("!Carga completa!\n")
    time.sleep(.5)
    return percent


def principal():

    valores_vel=[[15,20],[25,30]]
    percent = 0
    snake_coordinates =[200,100]
    snake_body = [[100,50],[90,50],[80,50]]
    pos_fruta = posicion_fruta()
    cambio = "RIGHT"
    run = True
    score = 0

    loading(percent)

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

        snake_body.insert(0, list(snake_coordinates))
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
            snake_body.pop()

        cabeza = snake_body[-1]
        for i in range(len(snake_body) - 1):
            part = snake_body[i]
            if cabeza[0] == part[0] and cabeza[1] == part[1]:
                run = False
                print("PERDISTE")
                menu(superficie_juego, text, instru, instru2, instru3)
                
        superficie_juego.fill((0,0,0))

        for pos in snake_body:
            pygame.draw.rect(superficie_juego,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(superficie_juego,(169,6,6), pygame.Rect(pos_fruta[0], pos_fruta[1], 10, 10))

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
    
    principal()


menu(superficie_juego, text, instru, instru2, instru3)

pygame.quit


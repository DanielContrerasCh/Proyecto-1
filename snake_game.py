#librerías necesarias
import pygame, sys, time, random

#Estado inicial
pygame.init()
superficie_juego= pygame.display.set_mode((500,500))

font = pygame.font.Font(None, 30)

fps = pygame.time.Clock()
    # print("Bienvenidos al juego de la serpiente, usa las flechas para moverte")
    # print("presione una flecha para empezar")

#coordenadas y valores iniciales
def posicion_fruta():

    posicion_random = random.randint (0,49)*10
    pos_fruta = [posicion_random, posicion_random]
    return pos_fruta

def puntuacion():
    puntaje = 0
    puntaje += 1
    print(puntaje)
    if puntaje < 10:
        fps.tick(10)
    if puntaje >= 10:
        fps.tick(20)


def principal():

    snake_coordinates =[200,100]
    snake_body = [[100,50],[90,50],[80,50]]
    pos_fruta = posicion_fruta()
    cambio = "RIGHT"
    run = True
    # puntaje = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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

        if snake_coordinates == pos_fruta:
            pos_fruta = posicion_fruta()
            puntuacion()
        else:
            snake_body.pop()

        cabeza = snake_body[-1]
        for i in range(len(snake_body) - 1):
            part = snake_body[i]
            if cabeza[0] == part[0] and cabeza[1] == part[1]:
                run = False
                print("Perdiste")

        superficie_juego.fill((0,0,0))

        for pos in snake_body:
            pygame.draw.rect(superficie_juego,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(superficie_juego,(169,6,6), pygame.Rect(pos_fruta[0], pos_fruta[1], 10, 10))

        text = font.render(puntuacion(),0,(200,60,80))
        superficie_juego.blit(text, (480,20))



        if snake_coordinates[0] <= 0 or snake_coordinates[0] >= 500:
            run = False
            print("YOU LOSE")
        if snake_coordinates[1] <= 0 or snake_coordinates[1] >= 500:
            run = False
            print("YOU LOSE")


        pygame.display.flip()

principal()

pygame.quit()



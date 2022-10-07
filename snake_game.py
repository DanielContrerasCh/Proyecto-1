#hay que correr "pip install pygame" y "pip install replit" en la consola para poder importar pygame, 
#librerías necesarias
import pygame, sys, time, random, replit

#Estado inicial
pygame.init()
superficie_juego= pygame.display.set_mode((500,500))
loading_screen = pygame.display.set_mode((500,500))

font = pygame.font.Font(None, 30)

fps = pygame.time.Clock()
    # print("Bienvenidos al juego de la serpiente, usa las flechas para moverte")
    # print("presione una flecha para empezar")

#coordenadas y valores iniciales
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
        bienvenida = print("""
    Pantalla de carga
    En el juego, utiliza las flechas para moverte\n

    Estatus: cargando
    %"""+ str(percent)
            )
        time.sleep(.05)

    carga = font.render(str(percent),0,(200,60,80))
    loading_screen.blit(carga, (480,20))
        
    terminado = print("!Carga completa!\n")
    return percent, terminado, bienvenida



def principal():

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
        if score < 5:
            fps.tick(20)
        elif score >=5:
            fps.tick(30)
        elif score >= 10:
            fps.tick(40)

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

        superficie_juego.fill((0,0,0))

        for pos in snake_body:
            pygame.draw.rect(superficie_juego,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(superficie_juego,(169,6,6), pygame.Rect(pos_fruta[0], pos_fruta[1], 10, 10))

        text = font.render(str(score),0,(200,60,80))
        superficie_juego.blit(text, (480,20))
        # carga = font.render(str(percent),0,(200,60,80))
        # superficie_juego.blit(carga, (250,250))



        if snake_coordinates[0] <= 0 or snake_coordinates[0] >= 500:
            run = False
            print("PERDISTE")
        if snake_coordinates[1] <= 0 or snake_coordinates[1] >= 500:
            run = False
            print("PERDISTE")


        pygame.display.flip()

principal()

pygame.quit()



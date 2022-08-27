#Estado inicial 
print("Bienvenidos al juego de la serpiente, usa las flechas para moverte")
print("presione una flecha para empezar")

#coordenadas iniciales
import random
snake_coordinates = (9,9)
apple_coordinates = random.randint(1,18)
#Mostrar puntajes
snake_size = (2)
puntaje = 0


#contador y tamaño de la serpiente
if snake_coordinates == apple_coordinates:
    puntaje + 1
    snake_size + 1
print(puntaje)

    

#Movimiento de la serpiente (Aún no lo descifro)
import keyboard
from pygame import K_LEFT, K_UP, K_DOWN, K_RIGHT

while True:
    if keyboard.read_key(K_LEFT):
        print("presionaste flecha izquierda")
    elif keyboard.read_key(K_RIGHT):
        print("presionaste flecha derecha")
        


    
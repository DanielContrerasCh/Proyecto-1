# Snake game
## Contexto
"Un juego adictivamente simple, Snake, fue lanzado, en 1997 con el Nokia 6110, seguía la idea básica de alargar un reptil que se movía más rápido mientras consumía más comida en la pantalla, pero moría si colisionaba consigo misma.
El concepto del juego de la serpiente se originó del juego de arcade de 1976, llamado Blockade, desarrollado por una compañía Británica llamda Gremlin Interactive, que cerró en 1984. Blockade fue diseñado como un juego de dos jugadores en el cuál cada uno guiaría sus propias serpientes, dejando detrás de ellos una línea sólida, la línea actuaba como un bloqueo y el jugador que duraba más sería el ganador." Fuente: https://theprint.in/features/nokias-snake-the-mobile-game-that-became-an-entire-generations-obsession/462873/#:~:text=The%20concept%20of%20Snake%20originated,a%20solid%20line%20behind%20them.

Además de que también marcó un antes y un después en la historia de los juegos móviles y se volvió la obsesión de una generación entera, este juego representó el despertar por mi interés en los videjuegos, ya que mi padre tenía un nokia con el Snake II, y recuerdo cómo solía pasar el tiempo tratando de batir mis récords.

## Algoritmos 
area_de_juego == 19 cuadros x 19 cuadros
  
Var tamaño_snake = 2 cuadros

  Var velocidad_snake =  adelante 3 cuadros/segundo
  
  Movimiento_snake:
  
    Rastrear y seguir recorrido de cabeza_snake
    
  Esperar tecla (flecha arriba) 
  
    Si direccion_snake = derecha = girar 90 grados izquierda
    
      else if direccion_snake = izquierda = girar 90 grados derecha
      
      else if direccion_snake = abajo = no girar
      
      else if direccion_snake = arriba = no girar
      
  Esperar tecla (flecha abajo)
  
    Si direccion_snake = derecha = girar 90 grados derecha
    
      else if direccion_snake = izquierda = girar 90 grados izquierda
      
      else if direccion_snake = arriba = no girar
      
      else if direccion_snake = abajo = no girar
      
Esperar tecla (flecha derecha)

      Si direccion_snake = derecha = no girar
      
        else if direccion_snake = izquierda = no girar
        
        else if direccion_snake = arriba = girar 90 grados derecha
        
        else if direccion_snake = abajo = girar 90 grados izquierda
        
Esperar tecla (flecha izquierda)

      Si direccion_snake = derecha = no girar
      
        else if direccion_snake = izquierda = no girar
        
        else if direccion_snake = arriba = girar 90 grados izquierda
        
        else if direccion_snake = abajo = girar 90 grados derecha
        
Var coordenadas_manzana:

      coordenadas_manzana = Aleatorio (x, y)
      
    Else coordenadas_cabeza_snake = coordenadas_manzana
    
       tamaño_snake = tamaño_snake + 1
       
       repite coordenadas_manzana
       
    Else if
    
       coordenadas_cabeza_snake = coordenadas_cuerpo_snake
       
    entonces str("game over"), termina juego
    
    Else if
    
       coordenadas_cabeza_snake = afuera de area_de_juego


  

